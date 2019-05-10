import sys
import time
from concurrent import futures
import grpc

sys.path.insert(0, 'service_spec')

import srl_pb2
import srl_pb2_grpc

import allen_srl

class SRLServicer(srl_pb2_grpc.SRLServicer):
    def resolve(self, request, context):
        if request.document is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("document is required!")
            return srl_pb2.Output()

        elif request.document == "":
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("document is empty!")
            return srl_pb2.Output()

        response = srl_pb2.Output()

        result = allen_srl.SRL.get_srl(request.document)

        if result is None:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("document is invalid.")
            return srl_pb2.Output()

        try:
            for verbs_dic in result['verbs']:
                ver = srl_pb2.Verbs()
                for tag in verbs_dic['tags']:
                    ver.tags.word.append(tag)
                response.verbs.add(verb=verbs_dic['verb'], description=verbs_dic['description'], tags=ver.tags)
            for word in result['words']:
                response.words.word.append(word)
        except Exception as exp:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details("Exception happened during getting results... \n", exp.__str__())
            return srl_pb2.Output()

        return response

def get_server(port="50051"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    srl_pb2_grpc.add_SRLServicer_to_server(SRLServicer(), server)
    server.add_insecure_port('[::]:' + str(port))
    return server

if __name__ == "__main__":
    server = get_server()
    server.start()
    print("Server has started on port:", "50051")
    _ONE_DAY = 86400
    try:
        while True:
            time.sleep(_ONE_DAY)
    except KeyboardInterrupt:
        server.stop(1)

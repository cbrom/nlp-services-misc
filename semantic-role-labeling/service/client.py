import os
import sys
import time
import grpc

sys.path.insert(0, 'service_spec')
import srl_pb2, srl_pb2_grpc

class TestSRLClient():
    def setUP(self):
        self.examples = [
            "The keys, which were needed to access the building, were locked in the car.",
            "However, voters decided that if the stadium was such a good idea someone would build it himself, and rejected it 59% to 41%.",
            "Did Uriah honestly think he could beat the game in under three hours?",
            "If you liked the music we were playing last night, you will absolutely love what we're playing tomorrow!",
            "More than a few CEOs say the red-carpet treatment tempts them to return to a heartland city for future meetings.",
        ]

        self.port = "50051"

    def test_grpc_call(self):
        self.setUP()

        with grpc.insecure_channel('localhost:' + self.port) as channel:
            stub = srl_pb2_grpc.SRLStub(channel)
            response1 = self.rpc_call(stub, self.examples[0])
            print(response1)


    def rpc_call(self, stub, document):
        request = srl_pb2.Input(document=document)
        response = stub.resolve(request)
        return response

if __name__ == "__main__":
    tc = TestSRLClient()
    tc.test_grpc_call()
import sys
import json
import unittest

import grpc
from google.protobuf.json_format import MessageToJson, MessageToDict

sys.path.insert(0, 'service')
sys.path.insert(0, 'service_spec')

from server import *
import srl_pb2, srl_pb2_grpc


class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
        self.examples = [
            "The keys, which were needed to access the building, were locked in the car.",
            "However, voters decided that if the stadium was such a good idea someone would build it himself, and rejected it 59% to 41%.",
            "Did Uriah honestly think he could beat the game in under three hours?",
            "If you liked the music we were playing last night, you will absolutely love what we're playing tomorrow!",
            "More than a few CEOs say the red-carpet treatment tempts them to return to a heartland city for future meetings.",
        ]
        with open('test_results.txt', 'r') as f:
            self.expected_result = json.load(f)

        self.port = "8001"
        self.result = []

        self.server = get_server(self.port)
        self.server.start()

    def test_grpc_call(self):
        with grpc.insecure_channel('localhost:' + self.port) as channel:
            stub = srl_pb2_grpc.SRLStub(channel)

            self.results = [MessageToDict(self.rpc_call(stub, example), including_default_value_fields=True) for example in self.examples]
            self.assertMultiLineEqual(str(self.results), str(self.expected_result))


    def rpc_call(self, stub, document):
        request = srl_pb2.Input(document=document)
        response = stub.resolve(request)
        return response

    def tearDown(self):
        self.server.stop(0)


if __name__=="__main__":
    unittest.main()
import sys
import argparse
from allennlp.predictors import Predictor

class SRL:
    # predictor = Predictor.from_path("/root/.allennlp/models/srl-model-2018.05.25.tar.gz")
    predictor = Predictor.from_path("./models/srl-model-2018.05.25.tar.gz")

    @staticmethod
    def get_srl(document):
        if SRL.validate_doc(document):
            return SRL.predictor.predict(document)

    @staticmethod
    def validate_doc(document):
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--document', '-d', help="Enter the document for Semantic Role Labeling")
    args = parser.parse_args()
    if args.document == None:
        print("Please enter the document. Terminating process...")
        sys.exit(0)
    print(args.document)

    print(SRL.get_srl(args.document))
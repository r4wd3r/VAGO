import argparse


class InputParser():
    def __init__(self):
        self.args = None

    def createParser(self):
        header = "____________\n"
        header += "V A G O  v1.0\n"
        header += "____________\n"

        print header

        parser = argparse.ArgumentParser(
            description="Vamos a vagar...")
        parser.add_argument("input_file", help='File to process', type=str)
        parser.add_argument('-o', '--output', help='Prefix name for output files.', type=str, default="output")

        args = parser.parse_args()

        '''
        filename = args.input_file
        output = args.output
        '''

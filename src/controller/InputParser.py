import argparse
import os
from src.view.InputParserOutput import InputParserOutput


class InputParser():
    def __init__(self):
        self.inputParserOutput = InputParserOutput()
        self.input_file_path = ""
        parser = argparse.ArgumentParser(
            description='Visual Advanced Graphicator Oooooooof Passwords... ',
            usage='''./vago.py <args> input_file''')

        parser.add_argument('input_file', help='Archivo a procesar', type=str, action='store')
        args = parser.parse_args()

        self.check_if_file_exists(args.input_file)

    def check_if_file_exists(self, path):

        if not os.path.exists(path):
            self.inputParserOutput.print_error_file_does_not_exist()
        else:
            self.input_file_path = str(path)

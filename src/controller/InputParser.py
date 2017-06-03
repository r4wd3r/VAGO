# encoding=utf-8

import argparse
import os
from src.view.InputParserOutput import InputParserOutput


class InputParser():
    '''Clase encargada de gestionar el parser'''

    def __init__(self):
        # TODO: Ajustar encapsulamiento de variable input_file_path
        self.inputParserOutput = InputParserOutput()
        self.inputParserOutput.print_header()
        parser = argparse.ArgumentParser(
            description='Visual Advanced Graphicator Oooooooof Passwords... ',
            usage='''./vago.py <args> input_file''')

        parser.add_argument('input_file', help='Archivo a procesar', type=str, action='store')
        self.args = parser.parse_args()

    def check_if_file_exists(self):
        path = self.args.input_file
        if not os.path.exists(path):
            self.inputParserOutput.print_error_file_does_not_exist()
            return ""
        else:
            return str(path)

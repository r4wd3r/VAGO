# encoding=utf-8

import argparse
from argparse import RawTextHelpFormatter
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
            usage='''./vago.py <args> input_file''', formatter_class=RawTextHelpFormatter)

        parser.add_argument('input_file', help='Archivo de passwords a procesar.', type=str, action='store')
        parser.add_argument('-o', '--output', help='Nombre de archivos de salida.', type=str, default="output")
        parser.add_argument('-f', '--filetype',
                            help='Formato del archivo de entrada (0 por defecto):\n'
                                 ' 0. password \n '
                                 '1. hash:password\n '
                                 '2. user:hash:password\n',
                            type=int, choices=range(0, 3), default=0)
        parser.add_argument('--history',
                            help='Informa si el archivo tiene formato de historiales '
                                 'basado en la salida de dsusers.py (user_nthistory0:hash:password, user_nthistory1:hash:password, ...)',
                            action="store_true")
        self.args = parser.parse_args()

    def check_if_file_exists(self):
        path = self.args.input_file
        if not os.path.exists(path):
            self.inputParserOutput.print_error_file_does_not_exist()
            return ""
        else:
            return str(path)

    def get_file_type(self):
        return self.args.filetype

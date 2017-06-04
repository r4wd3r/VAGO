# encoding=utf-8

import codecs
import sys
from src.view.FileProcessingOutput import FileProcessingOutput


class FileProcessing():
    def __init__(self):
        self.fileProcessingOutput = FileProcessingOutput()

    def read_input_file(self, file_path, file_type):
        '''
        Lectura de archivo y procesamiento de archivos
        :param file_path:
        :return: file_lines
        '''

        file_lines = []
        line_counter = 0
        self.fileProcessingOutput.print_reading_file(file_path)
        try:
            with codecs.open(file_path, encoding='utf8') as f:
                for l in f:
                    line_counter += 1
                    line = l.strip().encode("utf-8")
                    if line != "":
                        if self.check_line_format(line, file_type, line_counter):
                            file_lines.append(line)
            self.fileProcessingOutput.print_input_file_lines(len(file_lines))
        except:
            self.fileProcessingOutput.print_error_reading_file()
            sys.exit()

        if not file_lines:
            self.fileProcessingOutput.print_error_reading_file()
            sys.exit()
        return file_lines

    def check_line_format(self, line, file_type, line_counter):
        '''
        Verifica que la linea se ajuste al formato de proceso, y al tipo de archivo ingresado
        :param line: Linea a procesar
        :param file_type: Tipo de archivo
        :param line_counter: Contador de linea, para notificar en caso de error.
        :return: Retorna si la linea cumple o no con el formato establecido.
        '''

        if file_type == 0:
            return True
        elif file_type == 1:
            if not ':' in line:
                self.fileProcessingOutput.print_error_delimiter_not_found(line_counter)
                sys.exit()
            return True
        elif file_type == 2:
            if not ':' in line:
                self.fileProcessingOutput.print_error_delimiter_not_found(line_counter)
                sys.exit()
            _splitted_line = line.split(':')
            if len(_splitted_line) < 3:
                self.fileProcessingOutput.print_error_format_not_correct(line_counter)
                sys.exit()
            return True

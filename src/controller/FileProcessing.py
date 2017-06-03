# encoding=utf-8

import codecs
from src.view.FileProcessingOutput import FileProcessingOutput


class FileProcessing():
    def __init__(self):
        self.fileProcessingOutput = FileProcessingOutput()

    def read_input_file(self, file_path):
        '''
        Lectura de archivo y procesamiento de archivos
        :param file_path:
        :return: file_lines
        '''

        file_lines = []
        self.fileProcessingOutput.print_reading_file(file_path)
        try:
            with codecs.open(file_path, encoding='utf8') as f:
                for l in f:
                    line = l.strip().encode("utf-8")
                    if line != "":
                        file_lines.append(line)
        except:
            self.fileProcessingOutput.print_error_reading_file()
            return file_lines

        if not file_lines:
            self.fileProcessingOutput.print_error_reading_file()
            return file_lines
        return file_lines

from src.model.WorkData import WorkData
from src.model.Password import Password
from InputParser import InputParser
from FileProcessing import FileProcessing
from DataProcessing import DataProcessing

import sys


class VagoCore():
    '''Controlador principal definido para procesar los datos'''

    def __init__(self):
        self.inputParser = InputParser()
        self.workData = WorkData()
        self.fileProcessing = FileProcessing()
        self.dataProcessing = DataProcessing()

    def run(self):
        self.process_input_file()

    def process_input_file(self):
        '''
        Lectura del archivo y almacenamiento en la clase WorkData
        Lee el archivo y almacena las lineas en la lista workdata.input_file_lines
        '''
        _check_file_result = self.inputParser.check_if_file_exists()
        if _check_file_result:
            self.workData.input_file_path = _check_file_result
            _input_file_lines = self.fileProcessing.read_input_file(self.workData.input_file_path)
            if _input_file_lines:
                self.workData.input_file_lines = _input_file_lines
            else:
                sys.exit()
        else:
            sys.exit()

    def prepare_workdata(self):
        '''
        Prepara al objeto workdata que contiene los datos necesarios para generar los archivos para graficar
        '''

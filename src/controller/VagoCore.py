# encoding=utf-8

from src.model.WorkData import WorkData
from src.model.Password import Password
from src.view.VagoCoreOutput import VagoCoreOutput
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
        self.vagoCoreOutput = VagoCoreOutput()

    def run(self):
        self.process_input_file()
        self.prepare_workdata()

    def process_input_file(self):
        '''
        Lectura del archivo y almacenamiento en la clase WorkData
        Lee el archivo y almacena las lineas en la lista workdata.input_file_lines
        '''

        # Mostrar en pantalla proceso iniciado#
        self.vagoCoreOutput.print_input_file_processing_started()
        # -------------------------------------#

        _check_file_existance_result = self.inputParser.check_if_file_exists()
        if _check_file_existance_result:
            self.workData.input_file_path = _check_file_existance_result
            self.workData.input_file_type = self.inputParser.get_file_type()
            _input_file_lines = self.fileProcessing.read_input_file(self.workData.input_file_path,
                                                                    self.workData.input_file_type)
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

        # Mostrar en pantalla proceso iniciado#
        self.vagoCoreOutput.print_work_data_processing_started()
        # -------------------------------------#

        self.workData.number_of_lines = len(self.workData.input_file_lines)
        self.workData.passwords_table = self.dataProcessing.convert_to_password_hashtable(
            self.workData.input_file_lines,
            self.workData.input_file_type)
        self.workData.number_of_passwords = len(self.workData.passwords_table)

        # Ejemplo de impresión
        for _key in self.workData.passwords_table:
            print _key + ":" + str(self.workData.passwords_table[_key].freq) + ":" + str(
                self.workData.passwords_table[_key].text) + ":" + str(
                self.workData.passwords_table[_key].mask) + ":" + str(self.workData.passwords_table[_key].hash)

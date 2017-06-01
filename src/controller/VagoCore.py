from src.model.WorkData import WorkData
from InputParser import InputParser


class VagoCore():
    '''Controlador principal definido para procesar los datos'''

    def __init__(self):
        self.inputParser = InputParser()
        self.workData = WorkData()

    def run(self):
        if not self.inputParser.input_file_path:
            pass
        else:
            print "Begin the process"

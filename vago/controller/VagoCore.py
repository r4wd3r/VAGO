from InputParser import InputParser


class VagoCore():
    def __init__(self):
        self.inputParser = InputParser()


    def run(self):
        self.inputParser.createParser()


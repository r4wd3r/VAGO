import codecs
from src.view.FileProcessingOutput import FileProcessingOutput


class FileProcessing():
    def __init__(self):
        self.fileProcessingOutput = FileProcessingOutput()
        self.file_lines = []

    def read_file(self, file_path):
        self.fileProcessingOutput.print_reading_file(file_path)
        try:
            f = codecs.open(file_path, 'r', "utf-8")
            lines = f.readlines()
            f.close()
            print lines
        except:
            self.fileProcessingOutput.print_error_reading_file()

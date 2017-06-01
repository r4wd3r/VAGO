import codecs
from src.view.FileProcessingOutput import FileProcessingOutput


class FileProcessing():
    def __init__(self):
        self.fileProcessingOutput = FileProcessingOutput()
        self.file_lines = []

    def read_file(self, file_path):
        self.fileProcessingOutput.print_reading_file(file_path)
        try:
            with codecs.open(file_path, encoding='utf8') as f:
                for line in f:
                    self.file_lines.append([line.strip()])
            print self.file_lines
        except:
            self.fileProcessingOutput.print_error_reading_file()

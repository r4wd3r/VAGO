class FileProcessingOutput():
    def __init__(self):
        # STANDARD OUTPUT
        self.READING_FILE_MESSAGE = "[-] Reading the file: "
        self.INNPUT_FILE_LINES_MESSAGE = "[-] No. of lines: "
        # ERRORS
        self.ERROR_READING_FILE = "ERROR: Cannot read the file. Maybe it is not in VAGO format or is empty."

    def print_error_reading_file(self):
        print self.ERROR_READING_FILE

    def print_reading_file(self, filepath):
        print self.READING_FILE_MESSAGE + filepath

    def print_input_file_lines(self, lines):
        print self.INNPUT_FILE_LINES_MESSAGE + str(lines)
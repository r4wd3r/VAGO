class FileProcessingOutput():
    def __init__(self):
        # STANDARD OUTPUT
        self.READING_FILE_MESSAGE = "[-] Reading the file: "
        self.INNPUT_FILE_LINES_MESSAGE = "[-] No. of lines: "
        # ERRORS
        self.ERROR_READING_FILE = "ERROR: Cannot read the file. Maybe it is not in VAGO format or is empty."
        self.ERROR_DELIMITER_NOT_FOUND = "ERROR: Cannot find the ':' char. Line: "
        self.ERROR_FORMAT_NOT_CORRECT = "ERROR: File is not in the filetype format entered. Line: "

    def print_error_reading_file(self):
        print self.ERROR_READING_FILE

    def print_reading_file(self, filepath):
        print self.READING_FILE_MESSAGE + filepath

    def print_input_file_lines(self, lines_number):
        print self.INNPUT_FILE_LINES_MESSAGE + str(lines_number)

    def print_error_delimiter_not_found(self, line_number):
        print self.ERROR_DELIMITER_NOT_FOUND + str(line_number)

    def print_error_format_not_correct(self, line_number):
        print self.ERROR_FORMAT_NOT_CORRECT + str(line_number)

class FileProcessingOutput():
    def __init__(self):
        # STANDARD OUTPUT
        self.READING_FILE = "Reading the file: "
        # ERRORS
        self.ERROR_READING_FILE = "ERROR: Cannot read the file. Maybe it is not in VAGO format or is empty."

    def print_error_reading_file(self):
        print self.ERROR_READING_FILE

    def print_reading_file(self, filepath):
        print self.READING_FILE + filepath
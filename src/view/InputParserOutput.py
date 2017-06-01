class InputParserOutput():
    def __init__(self):
        self.ERROR_FILE_DOES_NOT_EXIST = "ERROR: Cannot open the file. File does not exist."

    def print_header(self):
        print "---------------\n"
        print "V A G O    v1.0\n"
        print "---------------\n"

    def print_error_file_does_not_exist(self):
        print self.ERROR_FILE_DOES_NOT_EXIST


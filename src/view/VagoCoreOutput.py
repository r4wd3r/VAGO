class VagoCoreOutput():
    def __init__(self):

        self.INPUT_FILE_PROCESSING_STARTED_MESSAGE = "\n[+] STARTING INPUT FILE PROCESSING"
        self.WORK_DATA_PROCESSING_STARTED_MESSAGE = "\n[+] STARTING WORKDATA PROCESSING"
        self.FILE_TYPE_MESSAGE = "[-] File type: "

    def print_input_file_processing_started(self):
        print self.INPUT_FILE_PROCESSING_STARTED_MESSAGE

    def print_work_data_processing_started(self):
        print self.WORK_DATA_PROCESSING_STARTED_MESSAGE

    def print_file_type_message(self,file_type):
        if file_type == 0:
            print self.FILE_TYPE_MESSAGE + str(file_type) + (" - Format: 'password'")
        elif file_type == 1:
            print self.FILE_TYPE_MESSAGE + str(file_type) + (" - Format: 'hash:password'")
        elif file_type == 2:
            print self.FILE_TYPE_MESSAGE + str(file_type) + (" - Format: 'user:hash:password'")



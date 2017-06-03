class VagoCoreOutput():
    def __init__(self):
        self.INPUT_FILE_PROCESSING_STARTED_MESSAGE = "\n[+] STARTING INPUT FILE PROCESSING"
        self.WORK_DATA_PROCESSING_STARTED_MESSAGE = "\n[+] STARTING WORKDATA PROCESSING"

    def print_input_file_processing_started(self):
        print self.INPUT_FILE_PROCESSING_STARTED_MESSAGE

    def print_work_data_processing_started(self):
        print self.WORK_DATA_PROCESSING_STARTED_MESSAGE

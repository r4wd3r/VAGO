class WorkData():
    '''Almacena todos los datos de trabajo para procesar.'''

    def __init__(self):
        self.input_file_path = ""
        self.input_file_type = 0  # Valor por defecto 0, formato password.
        self.input_file_lines = []  # Lineas del archivo convertidas en lista
        self.number_of_passwords = 0
        self.number_of_lines = 0
        self.passwords_table = {}

    @property
    def input_file_path(self):
        return self.input_file_path

    @input_file_path.setter
    def input_file_path(self, value):
        self.input_file_path = value

    @property
    def input_file_type(self):
        return self.input_file_type

    @input_file_type.setter
    def input_file_type(self, value):
        self.input_file_type = value

    @property
    def input_file_lines(self):
        return self.input_file_lines

    @input_file_lines.setter
    def input_file_lines(self, value):
        self.input_file_lines = value

    @property
    def number_of_passwords(self):
        return self.number_of_passwords

    @number_of_passwords.setter
    def number_of_passwords(self, value):
        self.number_of_passwords = value

    @property
    def number_of_lines(self):
        return self.number_of_lines

    @number_of_lines.setter
    def number_of_lines(self, value):
        self.number_of_lines = value

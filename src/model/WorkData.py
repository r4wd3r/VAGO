class WorkData():
    '''Almacena todos los datos de trabajo para procesar.'''

    def __init__(self):
        self.number_of_passwords = 0
        self.number_of_lines = 0
        self.passwords_table = {}

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
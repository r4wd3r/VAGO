from src.view.DataProcessingOutput import DataProcessingOutput
from src.model.Password import Password

import string


class DataProcessing():
    def __init__(self):
        self.dataProcessingOutput = DataProcessingOutput()

    def convert_to_password_hashtable(self, file_lines, file_type):
        '''
        Dependiendo del valor de file_type, realiza la conversión especificada.
        '''
        hashtable = {}

        for _line in file_lines:
            _password = self.convert_line_to_password(_line, file_type)
        return hashtable

    def convert_line_to_password(self, line, file_type):
        password = Password()
        if file_type == 0:  # Formato "password"
            (pass_length, charset, simplemask_string, advancedmask_string, policy) = self.analyze_password(line)
            password.text = line
            password.length = pass_length
            password.mask = advancedmask_string
        return password

    def analyze_password(self, password):
        '''
        Clase extraida del modulo statsgen.py de PACK v0.0.3
        '''

        # Password length
        pass_length = len(password)

        # Character-set and policy counters
        digit = 0
        lower = 0
        upper = 0
        special = 0

        simplemask = list()
        advancedmask_string = ""

        # Detect simple and advanced masks
        for letter in password:

            if letter in string.digits:
                digit += 1
                advancedmask_string += "?d"
                if not simplemask or not simplemask[-1] == 'digit': simplemask.append('digit')

            elif letter in string.lowercase:
                lower += 1
                advancedmask_string += "?l"
                if not simplemask or not simplemask[-1] == 'string': simplemask.append('string')


            elif letter in string.uppercase:
                upper += 1
                advancedmask_string += "?u"
                if not simplemask or not simplemask[-1] == 'string': simplemask.append('string')

            else:
                special += 1
                advancedmask_string += "?s"
                if not simplemask or not simplemask[-1] == 'special': simplemask.append('special')

        # String representation of masks
        simplemask_string = ''.join(simplemask) if len(simplemask) <= 3 else 'othermask'

        # Policy
        policy = (digit, lower, upper, special)

        # Determine character-set
        if digit and not lower and not upper and not special:
            charset = 'numeric'
        elif not digit and lower and not upper and not special:
            charset = 'loweralpha'
        elif not digit and not lower and upper and not special:
            charset = 'upperalpha'
        elif not digit and not lower and not upper and special:
            charset = 'special'

        elif not digit and lower and upper and not special:
            charset = 'mixedalpha'
        elif digit and lower and not upper and not special:
            charset = 'loweralphanum'
        elif digit and not lower and upper and not special:
            charset = 'upperalphanum'
        elif not digit and lower and not upper and special:
            charset = 'loweralphaspecial'
        elif not digit and not lower and upper and special:
            charset = 'upperalphaspecial'
        elif digit and not lower and not upper and special:
            charset = 'specialnum'

        elif not digit and lower and upper and special:
            charset = 'mixedalphaspecial'
        elif digit and not lower and upper and special:
            charset = 'upperalphaspecialnum'
        elif digit and lower and not upper and special:
            charset = 'loweralphaspecialnum'
        elif digit and lower and upper and not special:
            charset = 'mixedalphanum'
        else:
            charset = 'all'

        return (pass_length, charset, simplemask_string, advancedmask_string, policy)

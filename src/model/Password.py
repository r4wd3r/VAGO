import Algorithm


class Password():
    def __init__(self):
        self.id = 0
        self.text = None  # Contraseña en texto claro
        self.hash = None  # Hash equivalente de la contraseña
        self.length = 0  # Longitud de la contraseña
        self.freq = 0  # Repeticiones de la contraseña en el archivo
        self.complexity = 0  # Define el nivel de complejidad de la contraseña
        self.hashtype = Algorithm()  # Algoritmo de cifrado utilizado
        self.mask = None  # Máscara de la contraseña en formato hashcat

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self.id = value

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, value):
        self.text = value

    @property
    def hash(self):
        return self.hash

    @hash.setter
    def hash(self, value):
        self.hash = value

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, value):
        self.length = value

    @property
    def freq(self):
        return self.freq

    @freq.setter
    def freq(self, value):
        self.freq = value

    @property
    def complexity(self):
        return self.complexity

    @complexity.setter
    def complexity(self,value):
        self.complexity = value

    @property
    def mask(self):
        return self.mask

    @mask.setter
    def mask(self,value):
        self.mask = value

# encoding=utf-8

class Algorithm():
    def __init__(self):
        self.id = 0
        self.name = None

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self.id = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

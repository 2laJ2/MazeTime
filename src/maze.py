class Maze():
    def __init__(self, nimi: int):
        self._nimi = nimi

    def viesti(self):
        return "Hello, I'm a maze."

    def get_nimi(self):
        return self._nimi

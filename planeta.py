import json
class Planeta:
    def __init__(self, id, nome, clima, terreno, nro_filmes):
        self.id = id
        self.nome = nome
        self.clima = clima
        self.terreno = terreno
        self.nro_filmes = nro_filmes

    def adicionar_filmes(self, numero):
        self.nro_filmes = numero

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
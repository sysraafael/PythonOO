#Classe Mae

class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

#Classe Filha

class Animes(programa):
    def __init__(self, nome, ano, episodios):
        super().__init__(nome, ano)
        self.episodios = episodios

    def __str__(self):
        return f'Nome: {self.nome} - {self.episodios} min - Likes: {self.likes}'

#Classe Filha

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} min - Likes: {self.likes}'

jujutsukaisen = Animes('Jujutsu Kaisen', 2018, 24)
jujutsukaisen.dar_likes()
jujutsukaisen.dar_likes()
jujutsukaisen.dar_likes()

strangerthings = Serie('Stranger Things', 2016, 4)
strangerthings.dar_likes()
strangerthings.dar_likes()

listinha = [jujutsukaisen, strangerthings]

for programa in listinha:
    print(programa)

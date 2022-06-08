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
        return f'Nome: {self.nome} - {self.episodios} EP - Likes: {self.likes}'

#Classe Filha

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} TEMP - Likes: {self.likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


jujutsukaisen = Animes('Jujutsu Kaisen', 2018, 24)
strangerthings = Serie('Stranger Things', 2016, 4)
tokyorevengers = Animes('Tokyo Revengers', 2021, 24)
hunterxhunter = Animes('Hunter X Hunter', 1999, 148)

hunterxhunter.dar_likes()
hunterxhunter.dar_likes()
tokyorevengers.dar_likes()
tokyorevengers.dar_likes()
tokyorevengers.dar_likes()
jujutsukaisen.dar_likes()
jujutsukaisen.dar_likes()
jujutsukaisen.dar_likes()
strangerthings.dar_likes()
strangerthings.dar_likes()

listinha = [jujutsukaisen, strangerthings, tokyorevengers, hunterxhunter]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho da playlist: {len(minha_playlist)}')

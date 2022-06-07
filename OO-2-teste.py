class Animes:
    def __init__(self, nome, ano, episodios):
        self.__nome = nome.title()
        self.ano = ano
        self.episodios = episodios
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_nome):
        self.__nome = novo_nome.title()


jujutsuKaisen = Animes("Jujutsu Kaisen", 2018, 24)
jujutsuKaisen.dar_like()
jujutsuKaisen.dar_like()
print(f'Nome: {jujutsuKaisen.nome}, - Ano {jujutsuKaisen.ano} ' 

      f' - Episodios: {jujutsuKaisen.episodios} - Likes: {jujutsuKaisen.likes} ')


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.likes += 1

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_nome):
        self.__nome = novo_nome.title()


strangerthings = Serie("Stranger Things", 2016, 4)
strangerthings.dar_like()
print(f'Nome: {strangerthings.nome} - Ano: {strangerthings.ano} '
      f' - Temporadas {strangerthings.temporadas} - Likes: {strangerthings.likes} ')
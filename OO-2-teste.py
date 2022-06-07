class Animes:
    def __init__(self, nome, ano, episodios):
        self.nome = nome.title()
        self.ano = ano
        self.episodios = episodios
        self.likes = 0

    def dar_like(self):
        self.likes += 1


jujutsuKaisen = Animes("Jujutsu Kaisen", 2018, 24)
jujutsuKaisen.dar_like()
jujutsuKaisen.dar_like()
print(f'Nome: {jujutsuKaisen.nome}, - Ano {jujutsuKaisen.ano} ' 

      f' - Episodios: {jujutsuKaisen.episodios} - Likes: {jujutsuKaisen.likes} ')


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1


strangerthings = Serie("Stranger Things", 2016, 4)
strangerthings.dar_like()
print(f'Nome: {strangerthings.nome} - Ano: {strangerthings.ano} '
      f' - Temporadas {strangerthings.temporadas} - Likes: {strangerthings.likes} ')
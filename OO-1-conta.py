# Criando um objeto de conta bancaria como exemplo

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque 


    def saca(self, valor):
        if(self.__pode_sacar(valor)):   
            self.__saldo -= valor
        else:
            print('O valor ultrapassou o limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
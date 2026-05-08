class conta:
    # metodo construtor 
    def __init__(self, titular, agencia, numero):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = 0

    def extrato(self):
        print(f'o saldo do { self.__titular} é {self.__saldo}')

    def deposito(self, valor):
        self.__saldo = self.__saldo + valor

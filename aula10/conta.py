class conta:
    # metodo construtor 
    def __init__(self, titular, agencia, numero):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = f"{numero.randint(1000, 9999)}-{ random.randint(1,9)}"
        self.__cpf = cpf
        self.__saldo = 0
        self.__senha = random.randint(180000, 99999999)
        self.__chavepix = []

        @property
        def titular(self)
        return(self.__titular)

         @titular.setter
        def titular(self, novo_nome)
        self.__titular = novo_nome

         @property
        def agencia(self)
        return(self.__agencia)

         @property
        def numero(self)
        return(self.__numero)

         @property
        def saldo(self)
        return(self.__saldo)

         @property
        def cpf(self)
        return(self.__cpf)

         @property
        def chavepix(self)
        return(self.__chavepix)


    def extrato(self):
        print(f'o saldo do { self.__titular} é {self.__saldo}')

    def deposito(self, valor):
        self.__saldo = self.__saldo + valor

        def saque(self, valor)
        if valor <= self.__saldo and valor >0:
            self.__saldo = self.__saldo - valor
            print('saque efetuado com sucesso')
            else:
                print('erro ao efetuar o saque')
                def transferir(self, conta_destino, valor):
            self.__saque(valor)
            conta_destino.destino(valor)

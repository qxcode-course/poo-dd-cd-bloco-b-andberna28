class Pessoa:
    def __init__(self, nome: str, dinheiro: int = 0):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome
    def setNome(self, value: str):
        self.__nome = value
    def getDinheiro(self):
        return self.__dinheiro
    def setDinheiro(self, value: int):
        self.__dinheiro = value

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"

class Moto:
    def __init__(self):
        self.__custo: int = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
    
    def getCusto(self):
        return self.__custo
    def setCusto(self, value: str):
        self.__custo = value
    def getMotorista(self):
        return self.__motorista
    def setMotorista(self, value: int):
        self.__motorista = value
    def getPassageiro(self):
        return self.__passageiro
    def setPassageiro(self, value: int):
        self.__passageiro = value
    
    def __str__(self):
        mot = self.__motorista if self.__motorista else "None"
        pas = self.__passageiro if self.__passageiro else "None"
        return f"Cost: {self.__custo}, Driver: {mot}, Passenger: {pas}"
    
    def setDriver(self, motorista: Pessoa):
        if self.__motorista != None:
            print("fail: ja existe um motorista")
            return
        self.__motorista = motorista

    def setPassenger(self, passageiro: Pessoa):
        if self.__passageiro != None:
            print("fail: moto ocupada")
            return
        self.__passageiro = passageiro

    def drive(self, value: int):
        self.__custo += value

    def leavePass(self):
        if self.__passageiro == None:
            print("fail: nao ha passageiro")
            return
        passAnterior: Pessoa = self.__passageiro

        if self.__passageiro.getDinheiro() < self.__custo:
            print("fail: Passenger does not have enough money")

            self.__motorista.setDinheiro(self.__motorista.getDinheiro() + self.__custo)

            self.__passageiro.setDinheiro(0)
            self.__custo = 0
            self.__passageiro = None
            print (f"{passAnterior} left")
            return

        self.__passageiro.setDinheiro(self.__passageiro.getDinheiro() - self.__custo)
        self.__motorista.setDinheiro(self.__motorista.getDinheiro() + self.__custo)
        
        self.__custo = 0
        self.__passageiro = None
        print (f"{passAnterior} left")


def main():
    moto = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            motorista = args[1]
            dinheiroMot = int(args[2])
            moto.setDriver(Pessoa(motorista, dinheiroMot))
        elif args[0] == "setPass":
            passageiro = args[1]
            dinheiroPass = int(args[2])
            moto.setPassenger(Pessoa(passageiro, dinheiroPass))
        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            moto.leavePass()


main()
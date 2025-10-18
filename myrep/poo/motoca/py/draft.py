class Pessoa:
    def __init__(self, nome: str, idade: int = 0):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def setNome(self, value: str):
        self.__nome = value

    def getIdade(self):
        return self.__idade
    
    def setIdade(self, value: int):
        self.__idade = value

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
class Moto:
    def __init__(self):
        self.cliente: Pessoa | None = None
        self.tempo: int = 0
        self.potencia: int = 1

    def enter(self, cliente: Pessoa):
        if self.cliente != None:
            print("fail: busy motorcycle")
            return
        self.cliente = cliente

    def leave(self) -> Pessoa | None:
        if self.cliente == None:
            print("fail: empty motorcycle")
            return None
        clienteAnterior: Pessoa = self.cliente
        self.cliente = None
        return f"{clienteAnterior}"
    
    def comprar(self, increment: int):
        self.tempo += increment
        return
    
    def drive(self, tempo: int):
        if self.tempo == 0:
            print("fail: buy time first")
            return
        if self.cliente == None:
            print("fail: empty motorcycle")
            return
        if self.cliente.getIdade() > 10:
            print("fail: too old to drive")
            return
        if tempo > self.tempo:
            print(f"fail: time finished after {self.tempo} minutes")
            self.tempo = 0
            return
        self.tempo -= tempo
           
    def honk(self):
        print("P" + "e" * self.potencia + "m")

    def init(self, potencia: int = 1):
        self.cliente = None
        self.tempo = 0
        self.potencia = potencia
        return

    def __str__(self):
        cliente_str = "empty" if self.cliente == None else self.cliente
        return f"power:{self.potencia}, time:{self.tempo}, person:({cliente_str})"

def main():
    motoca = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            motoca.enter(Pessoa(nome, idade))
        elif args[0] == "init":
            potencia = int(args[1])
            motoca.init(potencia)
        elif args[0] == "leave":
            pessoa = motoca.leave()
            if pessoa:
                print(f"{pessoa}")
        elif args[0] == "buy":
            increment = int(args[1])
            motoca.comprar(increment)
        elif args[0] == "drive":
            tempo = int(args[1])
            motoca.drive(tempo)
        elif args[0] == "honk":
            motoca.honk()
        elif args[0] == "show":
            print(motoca)

main()
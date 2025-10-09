class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def __str__(self):
        return f"size: ({self.__tamanho})"

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

def main():
    roupa = Roupa()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "size":
            tamanho = args[1]
            roupa.setTamanho(tamanho)
        elif args[0] == "show":
            print(roupa)

main()
class Roupa:
    def __init__(self, tamanho: str = ""):
        self.tamanho: str = tamanho

    def __str__(self):
        return f"size: ({self.tamanho})"

    def setTamanho(self):
        if self.tamanho == "PP" and self.tamanho == "P" and self.tamanho == "M" and self.tamanho == "G" and self.tamanho == "GG" and self.tamanho == "XG":
            return self.tamanho



def main():
    roupa = Roupa()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "size":
            roupa.tamanho()
        elif args[0] == "show":
            print(roupa)

main()
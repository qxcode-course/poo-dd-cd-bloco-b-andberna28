class Lead:
    def __init__(self, thickness: float = 0, hardness: str = "", size: int = 0):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size: int = size

    def getThickness(self):
        return self.__thickness
    def getHardness(self):
        return self.__hardness
    def getSize(self):
        return self.__size
    def setSize(self, value: int):
        self.__size = value
        
    def init(self, thickness: float = 0, hardness: str = "", size: int = 0):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"


class Pencil:
    def __init__(self):
        self.tip: Lead | None = None
        self.thickness: float = 0.0

    def init(self, thickness: float):
        self.thickness = thickness

    def hasGrafite(self) -> bool:
        return self.tip is not None

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if lead.getThickness() != self.thickness:
            print("fail: calibre incompativel")
            return
        self.tip = lead

    def remove(self):
        self.tip = None

    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        gasto = 0
        if self.tip.getHardness() == "HB":
            gasto = 1
        elif self.tip.getHardness() == "2B":
            gasto = 2
        elif self.tip.getHardness() == "4B":
            gasto = 4
        elif self.tip.getHardness() == "6B":
            gasto = 6

        if self.tip.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        novo_tamanho = self.tip.getSize() - gasto
        if novo_tamanho < 10:
            self.tip.setSize(10)
            print("fail: folha incompleta")
            return

        self.tip.setSize(novo_tamanho)

    def __str__(self):
        if self.tip == None:
            return f"calibre: {self.thickness}, grafite: null"
        return f"calibre: {self.thickness}, grafite: {self.tip}"

def main():
    lapis = Pencil()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            calibre = float(args[1])
            lapis.init(calibre)
        elif args[0] == "insert":
            calibre = float(args[1])
            hardness = args[2]
            size = int(args[3])
            grafite = Lead(calibre, hardness, size)
            lapis.insert(grafite)
        elif args[0] == "remove":
            lapis.remove()
        elif args[0] == "write":
            lapis.write()
        elif args[0] == "show":
            print(lapis)

main()
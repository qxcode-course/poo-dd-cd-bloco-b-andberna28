class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho = valor
        else:
            print("Tá louco pai? Tá metendo o louco? Só tem 'PP', 'P', 'M' e 'G', 'GG' e 'XG'")

camisa = Camisa()
while camisa.getTamanho() == "":
    print("Digite seu tamanho de roupa")
    tamanho = input()
    camisa.setTamanho(tamanho)

print("Parabéns, você comprou uma camisa tamanho: ", camisa.getTamanho())
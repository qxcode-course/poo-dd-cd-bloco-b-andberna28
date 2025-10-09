class Chinela:
    def __init__(self):
        self.__tamanho = 0
    
    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor >= 20 and valor <= 50 and valor % 2 == 0:
            self.__tamanho = valor
        else:
            print("ronaldo")


chinela = Chinela()
while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)
print("Parabéns, você comprou uma chinela tamanho: ", chinela.getTamanho())


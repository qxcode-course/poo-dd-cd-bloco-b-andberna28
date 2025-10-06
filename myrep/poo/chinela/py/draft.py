class Chinela:
    def __init__(self, tamanho:int = 0):
        self.__tamanho = 0
    
    def setTamanho(self):
        if self.__tamanho >= 20 and self.__tamanho <= 50 and self.__tamanho % 2 == 0:
            print(self.__tamanho)
        else:
            print("ronaldo")


chinela = Chinela(input())
print(chinela)


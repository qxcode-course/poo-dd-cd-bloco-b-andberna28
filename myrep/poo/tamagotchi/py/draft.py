class Tamagochi:
    def __init__(self, energyMax: int = 0, cleanMax: int = 0):
        self.__energyMax = energyMax
        self.__cleanMax = cleanMax
        self.__energy = energyMax
        self.__clean = cleanMax
        self.__age: int = 0
        self.__alive: bool = True


    def getEnergyMax(self):
        return self.__energyMax

    def getCleanMax(self):
        return self.__cleanMax

    def getEnergy(self):
        return self.__energy

    def setEnergy(self, value: int):
        self.__energy = value
        if self.__energy <= 0:
            self.__energy = 0
            self.__alive = False
            print("fail: pet morreu de fraqueza")

    def getClean(self):
        return self.__clean

    def setClean(self, value: int):
        self.__clean = value
        if self.__clean <= 0:
            self.__clean = 0
            self.__alive = False
            print("fail: pet morreu de sujeira")

    def getAge(self):
        return self.__age

    def setAge(self, value: int):
        self.__age = value

    def getAlive(self):
        return self.__alive

    def __str__(self):
        return f"E:{self.__energy}/{self.__energyMax}, L:{self.__clean}/{self.__cleanMax}, I:{self.__age}"


class Game:
    def __init__(self):
        self.pet: Tamagochi | None = None

    def init(self, energyMax: int, cleanMax: int):
        self.pet = Tamagochi(energyMax, cleanMax)

    def __str__(self):
        if self.pet is None:
            return "fail: nenhum tamagochi criado"
        return str(self.pet)
    
    def play(self):
        if not self.pet.getAlive():
            print("fail: pet esta morto")
            return
        self.pet.setEnergy(self.pet.getEnergy() - 2)
        self.pet.setClean(self.pet.getClean() - 3)
        self.pet.setAge(self.pet.getAge() + 1)

    def sleep(self):
        if not self.pet.getAlive():
            print("fail: pet esta morto")
        if self.pet.getEnergy() > 15:
            print("fail: nao esta com sono")
            return
        self.pet.setEnergy(self.pet.getEnergyMax())
        self.pet.setAge(self.pet.getAge() + 6)

    def shower(self):
        if not self.pet.getAlive():
            print("fail: pet esta morto")
            return
        self.pet.setEnergy(self.pet.getEnergy() - 3)
        self.pet.setClean(self.pet.getCleanMax())
        self.pet.setAge(self.pet.getAge() + 2)

def main():
    game = Game()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(game)
        elif args[0] == "init":
            energyMax = int(args[1])
            cleanMax = int(args[2])
            game.init(energyMax, cleanMax)
        elif args[0] == "play":
            game.play()
        elif args[0] == "sleep":
            game.sleep()
        elif args[0] == "shower":
            game.shower()

main()

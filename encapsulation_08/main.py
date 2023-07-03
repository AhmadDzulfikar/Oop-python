class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__power = attackPower

    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter 
    def Damaged(self, damaged):
        self.__health -= damaged
    
    def setAttPower(self,damageMasuk):
        self.__power = damageMasuk

# awal dari game 
alu = Hero("Alucard", 50, 5)

# game berjalan
print(alu.getName())
print(alu.getHealth())

alu.Damaged(5)
print(alu.getHealth())
class Hero:

    def __init__(self, name, health, defense):
        self.name = name
        self.__health = health
        self.__defense = defense
        # self.info = "name {} : \n\thealth: {} \n\tdefense: {}".format(self.__name, self.__health, self.__defense)
    
    @property
    def info(self):
        return "name {} : \n\thealth: {} \n\tdefense: {}".format(self.name, self.__health, self.__defense)
    
    @property
    def defense(self):
        pass

    @defense.getter
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self, input):
        self.__defense = input

    @defense.deleter
    def armor(self):
        print('defense di hapus')
        self.__defense = None

alu = Hero('alucard', 100, 20)
print("Merubah Info")
print(alu.info)
alu.name = "Miya"
print(alu.info)

print("\ngetter and setter untuk defense:")

print(alu.defense)
print(alu.__dict__)

alu.defense = 10
print(alu.defense)
print(alu.__dict__)

print('hapus defense')
del alu.armor
print(alu.__dict__)
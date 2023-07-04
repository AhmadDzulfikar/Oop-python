class Hero:

    # private class variable
    __jumlah = 0 

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0 

        self.__healthMax = self.__healthBase * self.__level
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100 ):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level
    
    def attack(self, musuh):
        self.gainExp = 50


hobin = Hero('Hobin', 100, 5, 10)
jin = Hero('jin', 100, 5, 10)

print(hobin.info)
hobin.attack(jin)
hobin.attack(jin)
hobin.attack(jin)
hobin.attack(jin)


print(hobin.info)
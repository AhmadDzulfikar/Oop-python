# Static & Class Method

class Hero:

    # private class variable 
    __jumlah = 0;

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku ke objek, tapi berlaku ke class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
alu = Hero('Alucard')
print(Hero.getJumlah2())
vex = Hero('Vexana')
print(vex.getJumlah2())
gatot = Hero("Gatot Kaca")
print(Hero.getJumlah3())

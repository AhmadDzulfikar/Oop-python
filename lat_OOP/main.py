class Hero:

    def __init__(self, name, health, damage, stamina): #self = objek
        self.name = name
        self.health = health
        self.damage = damage
        self.stamina = stamina

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.damage)

    def diserang(self, lawan, damage_kita):
        print(self.name + " diserang " + lawan.name)
        damage_diterima = damage_kita/self.stamina
        print('serangan terasa : ' + str(damage_diterima))
        self.health -= damage_diterima 
        print("darah " + self.name + " tersisa " + str(self.health))

player1 = Hero('Kakashi', 10000, 450, 200)
player2 = Hero('Obito', 8000, 300, 150)

player1.serang(player2)
print("\n")
player2.serang(player1)


# inheritance = pewarisan 

class Hero:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health    
        self.power = power

class Hero_Heal(Hero):
    pass

class Hero_damage(Hero):
    pass

sakura = Hero("sage sakura", 100, 20)
sizune = Hero_Heal('sizune', 100, 20)
A = Hero_damage('A', 600, 300)

print(sakura.name)
print(sizune.name)
print(A.health)

#test
#e=tes
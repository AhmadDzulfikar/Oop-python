class Hero:
    #class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputAge, inputSkill):
        #instance variabel
        self.name = inputName
        self.age = inputAge
        self.skill = inputSkill
        Hero.jumlah_hero += 1

        # void function, method tanpa return & argumen  
    def siapa(self):
            print("namaku adalah " + self.name)

        # method dengan argumen, tanpa return
    def skillUp(self, up):
        self.skill += up

        # method dengan return
    def getSkill(self):
        return self.skill

hero1 = Hero('Hobin', 17, 'Muay Thai')
hero2 = Hero('Dzulfikar', 17, 'Kick Boxing')
# print(hero1.__dict__)

hero1.skillUp(' & taekwondo')
hero1.siapa()

hero2.skillUp(' & taekwondo')

# print(hero1.skill)

print(hero1.getSkill())
print(hero2.getSkill())
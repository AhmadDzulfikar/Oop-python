class Hero: # template
    #class variabel
    jumlah = 0

    def __init__(self, inputName, inputAge, inputSkill):
        # instance variable
        self.name = inputName
        self.age = inputAge
        self.skill = inputSkill
        Hero.jumlah += 1
        print('Membuat hero dengan nama ' + self.name)

hero1 = Hero("Hobin", 17, "all")
print(Hero.jumlah)
hero2 = Hero("Taehoon", 18, 'taekwondo')
print(Hero.jumlah)
hero3 = Hero("Park Hyungseok", 17, 'copy')
print(Hero.jumlah)
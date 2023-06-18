class Hero: # template

    def __init__(self, inputName, inputAge, inputSkill):
        self.name = inputName
        self.age = inputAge
        self.skill = inputSkill

hero1 = Hero("Hobin", 17, "all")
hero2 = Hero("Taehoon", 18, 'taekwondo')
hero3 = Hero("Park Hyungseok", 17, 'copy')

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
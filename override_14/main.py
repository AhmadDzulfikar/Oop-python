class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("mengambil info dari supclass")
        print("{} health : {}".format(
            self.name,
            self.health)
            )

class Hero_heal(Hero):
    # mengambil supclass
    def __init__(self, name):
        super().__init__(name,120)
        
    # override (menimpa dari supclass)
    def showInfo(self):
        print("mengambil info dari subclass")
        print("{} \n\tTipe: heal, \n\thealth : {}". format(
            self.name, self.health
        ))

class Hero_damage(Hero):
    def __init__(self, name):
        super().__init__(name,110)

sakura = Hero_heal('sage sakura')
ino = Hero_heal('ino')
kakashi = Hero_damage('kakashi')

sakura.showInfo()
ino.showInfo()

kakashi.showInfo() 
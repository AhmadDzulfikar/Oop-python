class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health {}".format(self.name, self.health))

# contoh tidak pengulangan (BENAR)
class Hero_heal(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 120) # NOTE: Kurang tepat
        super().__init__(name, 130) # NOTE: tepat, karena pake super(), 
                                    # NOTE: super = supclass (Hero)
        super().showInfo()
        # Hero.showInfo(self) # NOTE: kalau pake kayak begini semisal si subclass ganti supclass kita harus ganti si Hero.showInfo

# contoh perulangan (SALAH)
class Hero_damage(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 200

sakura = Hero_heal('sage sakura')
kakashi = Hero_damage('kakashi')

print('name :', sakura.name, " ", 'health :', sakura.health)
print('name :', kakashi.name, " ", 'health :', kakashi.health)

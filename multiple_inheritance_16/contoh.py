class Team:
    def set_team(self, team):
        self.team = team

    def show_team(self):
        print(self.team)

class HeroType:
    def set_type(self,type):
        self.type = type
    
    def show_type(self):
        print(self.type)

class Ninja(Team, HeroType):
    
    def __init__(self, name, health) :
        self.name = name
        self.health = health

Byron = Ninja('Byron', 250)
Byron.set_team('Red Team')
Byron.set_type('damage')

Byron.show_team()
Byron.show_type()




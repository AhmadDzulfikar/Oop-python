class Hero:
    def __init__(self, name):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attPower_pool = [0, 10, 20, 30, 40, 50 ]
        self.defense_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0 
        self.__level = 0 
    
    def show_info(self):
        print('{} \n\tlevel: {}, \n\thealth: {}, \n\tattPower: {}, \n\tdefense: {}'.format(
                self.__name,
                self.__level,
                self.__health,
                self.__attPower,
                self.__defense
                ))
        
    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def defense_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self, input):
        self.__health_pool = input

    @attPower_pool.setter
    def attPower_pool(self, input):
        self.__attPower_pool = input

    @defense_pool.setter
    def defense_pool(self, input):
        self.__defense_pool = input

    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp // 100
            self.__exp %= 100 

    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level] # NOTE : [] = list, () = tuple
        self.__defense = self.__defense_pool[self.__level]


class HeroHeal(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.attPower_pool = [0,5,10,15,20,25]
        self.defense_pool = [0,3,5,7,10,12]
        self.levelUp = 1

class HeroPower(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0,50,100,125,150,200]
        self.attPower_pool = [0,100,200,300,400,500]
        self.defense_pool = [0,5,9,13,15,17]
        self.levelUp = 1

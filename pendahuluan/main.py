class Hero: # template
    pass

hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Hobin'
hero1.skill = 'all'

hero2.name = 'Taehoon'
hero2.skill = 'taekwondo'

hero3.name = 'Park Hyungseok'
hero3.skill = 'copy'

print(hero1)
print(hero1.__dict__)
print(hero1.name)

print(hero1.name, 'vs', hero2.name )
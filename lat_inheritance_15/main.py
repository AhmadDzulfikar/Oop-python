from hero import HeroHeal, HeroPower # NOTE : fromnya samain sama modul isinya huruf besar kecilnya peratiin

sakura = HeroHeal('Sage Sakura')
obito = HeroPower('Obito')

sakura.show_info()
obito.show_info()

sakura.gainExp = 200 
obito.gainExp = 250

print('\n')
sakura.show_info()
obito.show_info()

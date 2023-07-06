class Squad:
    def __init__(self):
        self.__list_squad = []

    def tambah_anggota(self,name):
        self.__list_squad.append(name)

    def __len__(self):
        return len(self.__list_squad)
    
squad1 = Squad()
squad1.tambah_anggota('Pucay')
squad1.tambah_anggota('Fancy')
print(len(squad1))
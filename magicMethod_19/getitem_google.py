class Squad:
    def __init__(self):
        self.__list_anggota = []

    def tambah_anggota(self, anggota):
        self.__list_anggota.append(anggota)

    def __len__(self):
        return len(self.__list_anggota)
    
    def __getitem__(self,position):
        return self.__list_anggota[position]
    
squad1 = Squad()
squad1.tambah_anggota('Pucay')
squad1.tambah_anggota('Fancy')

print(squad1[0])
print(squad1[1])
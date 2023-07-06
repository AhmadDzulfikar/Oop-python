class Duren:
    # magic method 
    def __init__(self, nama, jumlah): # init adalah salah satu magic method
        self.nama = nama
        self.jumlah = jumlah


    ''' __repr & __str__ itu sama aja, tapiiii
        __str__ biasanya kalo programnya udah jadi & produksi
        __repr__ biasanya masih debugging
    '''

    def __repr__(self):
        return "(repr) Duren {} berjumlah {}".format(
            self.nama,
            self.jumlah)
    
    def __str__(self):
        return "(str) Duren {} berjumlah {}".format(
            self.nama,
            self.jumlah)

    def __add__(self, object):
        return self.jumlah + object.jumlah 
    
    # Masih banyak magic method lainnya GOOGLING!!!!!!

belanja1 = Duren('Montong', 2)
belanja2 = Duren('Musang King', 3)
belanja3 = Duren('Petruk', 4)
print(repr(belanja1))
print(belanja2)

print(belanja1 + belanja2)



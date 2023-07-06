class Segitiga:

    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    def __str__(self):
        luas = 0.5 * self.alas * self.tinggi
        return "segitiga (alas={} tinggi={} luas={})".format(self.alas,self.tinggi,luas)
# buat instan
a = Segitiga(10, 10)
b = Segitiga(20, 10)
print(a)
print(b)
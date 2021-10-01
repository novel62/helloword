# Masukkan sebuah bilangan
# Bagi bilangan tersebut dengan 2
# Jika sisa pembagian = 0 maka bilangan tersebut adalah bilangan genap
# Jika sisa pembagian = 1 maka bilangan tersebut adalah bilangan ganjil
bil = int(input('masukkan bilangan ='))
sisa = bil % 2
if sisa == 0:
    print('bilangan tersebut adalah genap')
else:
    print('sisa bagi 1,bilangan tersebut adalah ganjil')

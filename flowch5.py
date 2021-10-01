# Masukkan bilangan pertama
# Masukkan bilangan kedua
# Masukkan bilangan ketiga
# Jika b1 > b2 dan b1 > b3 maka cetak “ Bilangan Pertama adalah Bilangan Terbesar”
# Jika b2 > b1 dan b2 > b3 maka cetak “ Bilangan Kedua adalah Bilangan Terbesar”
# Cetak “Bilangan Ketiga adalah Bilangan Terbesar”
b1 = int(input('masukan bil1 ='))
b2 = int(input('masukan bil2 ='))
b3 = int(input('masukan bil3 ='))
if b1 > b2 and b1 > b3:
    print('maka bilangan b1 adalah terbesar=', b1)
elif b2 > b1 and b2 > b3:
    print('maka bilangan b2 adalah terbesar=', b2)
else:
    print('maka bilangan b3 adalah terbesar=', b3)

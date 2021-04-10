gaji1=int(input("masukan gaji pokok bulan :"))
gaji_thn=12*gaji
if gaji_thn>= 15600000:
  ket1='kena pajak'
else:
  ket1='tidak kena pajak'
 print('keterangannya adalah:',ket1)

def hitGaji(g):
  gaji=12*gaji
  print('gaji adalah:',gaji)
  if gaji >=15600000:
    ket='kena pajak'
  else:
    ket='Tidak kena pajak'
  print('keterangannya adl =',ket)
 hitGaji(2000000)

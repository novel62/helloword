gaji=int(input("masukan gaji pokok bulan :"))
gaji_thn=12*gaji
if gaji_thn>= 15600000:
  ket='kena pajak'
 else:
  ket='tidak kena pajak'
 print('keterangannya adalah:',ket)

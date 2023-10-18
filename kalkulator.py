print("===================[]")
print("KALKULATOR BY DILLON")
print("===================[]")
print("       × ÷ - +     ||")
print("x => Perkalian     ||")
print("t => Penjumlahan   ||")
print("k => Pengurangan   ||")
print("b => Pembagian     ||")
print('===================[]')
print('WALAUPUN BURIK TAPI WORKK=[]')
print('===================[]')
pilihanUser = input("pilih operasi : ")

# OPERASI DASAR
if ( pilihanUser == "x") :
 inputUser = int(input("Masukan Angka : "))
 inputKali = int(input("Masukan Kali : "))
 kali = inputUser * inputKali
 print("Hasil nya adalah : ",kali)
if ( pilihanUser == "t") :
 inputUser = int(input("Masukan Angka : "))
 inputTambah = int(input("Masukan Tambah : "))
 tambah = inputUser + inputTambah
 print("Hasil nya adalah : ",tambah)
if ( pilihanUser == "k") :
 inputUser = int(input("Masukan Angka : "))
 inputKurang = int(input("Masukan Kurang : "))
 kurang = inputUser - inputKurang
 print("Hasil nya adalah : ",tambah)
if ( pilihanUser == "b") :
 inputUser = int(input("Masukan Angka : "))
 inputBagi = int(input("Masukan Tambah : "))
 bagi = inputUser / inputBagi
 print("Hasil nya adalah : ",bagi)

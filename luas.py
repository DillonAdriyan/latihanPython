print("===================[]")
print("KALKULATOR BY DILLON")
print("===================[]")
print("      [] [ ] ∆ o   ||")
print("x =>     Kotak     ||")
print("t => PersegiPanj   ||")
print("k => segitiga      ||")
print("b => lingkaran     ||")
print('===================[]')
print('WALAUPUN BURIK TAPI WORKK=[]')
print('===================[]')
pilihanUser = input("pilih Bidang : ")
satuan = input("pilih satuan : ")
 # mencari Luas Persegi
if pilihanUser == "x"  :
 pilihanUser = "Persegi"
 inputUser = int(input("Masukan Panjang Sisi : "))
 kotak = inputUser * inputUser
 print("Luas Bidang Tersebut adalah : ", kotak, satuan,"²")
elif (pilihanUser == "t" ) :
 pilihanUser = "Persegi Panjang"
 inputUser1 = int(input("Masukan Panjang Sisi 1 : "))
 inputUser2 = int(input("Masukan Panjang Sisi 2 : "))
 perPan = (inputUser1 * inputUser2)
 print("Luas ", pilihanUser, "Tersebut adalah : ", perPan, satuan,"²")
elif (pilihanUser == "k" ) :
 pilihanUser = "Segitiga"
 inputUser1 = int(input("Masukan Panjang Alas : "))
 inputUser2 = int(input("Masukan Tinggi: "))
 segitiga = (1/2) * inputUser1 * inputUser2
 print("Luas ", pilihanUser, "Tersebut adalah : ", segitiga, satuan,"²")
elif (pilihanUser == "b" ) :
 phi = 3.1415
 pilihanUser = "Lingkaran"
 inputUser1 = int(input("Masukan Diameter : "))
 #inputUser2 = int(input("Masukan Tinggi : "))
 segitiga = phi * ((inputUser1 / 2) ** 2)
 print("Luas", pilihanUser, "Tersebut adalah : ", segitiga, satuan,"²")
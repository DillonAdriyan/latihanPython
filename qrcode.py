import segno
inputUser = input("Masukan Text/Url : ")
qrcode = segno.make_qr(inputUser)
qrcode.save(
 "dillon.png",
 scale=10,

)
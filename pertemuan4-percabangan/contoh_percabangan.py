#Input
kode_baju = input("Masukkan kode baju [SP/AD] : ")
ukuran = input("Masukkan ukuran baju [S/M] : ")

#Proses
if kode_baju == "SP" or kode_baju == "sp":
    merk = "Super Dry"
    if ukuran == "S" or ukuran == "s":
        harga = 450000
    elif ukuran == "M" or ukuran == "m":
        harga = 50000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 650000
    elif ukuran == "M" or ukuran == "m":
        harga = 70000
    else:
        harga = 0
else:
    merk = "Salah input kode"
    harga = 0
#Output
print("-------------------")
print("Merek Baju : ",str(merk))
print("Ukuran : ", ukuran)
print("Harga : Rp ", harga)
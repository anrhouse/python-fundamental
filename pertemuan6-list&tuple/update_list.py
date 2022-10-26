#ada yg salah
ganjil = [1,3,4,7,8,10]
print(ganjil)

#ubah index ke 2
ganjil[2] = 5
print(ganjil)

#mengubah dalam range tertentu
ganjil[4:6] = [9,11]
print(ganjil)

#menambah anggota
ganjil.append(13)
print(ganjil)

#menyisipkan list
ganjil.insert(1,10)
print(ganjil)

#menggabungkan list
tambah = [15,17,['a','b','c'],3]
ganjil = ganjil + tambah
print(ganjil)

#menghapus berdasarkan value
ganjil.remove(['a','b','c'])
print(ganjil)
ganjil.remove(3)
print(ganjil)

#hapus berdasarkan index
del ganjil[9]
print(ganjil)

#sorting
ganjil.sort(reverse=True) #desc
print(ganjil)
ganjil.sort(reverse=False) #asc
print(ganjil)

#pengecekan apakah value itu ada or tdk pada list
print(5 in ganjil)
print(4 in ganjil)
print("==============")
print(5 not in ganjil)
print(4 not in ganjil)

#iterasi pada list
for angka in ganjil:
    print(angka)
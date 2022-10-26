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

#menggabungkan list
tambah = [15,17]
ganjil = ganjil + tambah
print(ganjil)

#menyisipkan list
ganjil.insert(0,0)
print(ganjil)

#menghapus 0
ganjil.remove(0)
print(ganjil)
ganjil.remove(3)
print(ganjil)

#sorting
ganjil.sort(reverse=True)
print(ganjil)
ganjil.sort(reverse=False)
print(ganjil)
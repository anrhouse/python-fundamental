#input
pembeli = input("Input nama pembeli : ")
no_hp = input("Input no HP : ")
jurusan = input("Input jurusan : [SBY/BL/LMP] : ")
jummlah = int(input("Masukkan jumlah beli : "));

#proses penentuan jurusan & harga
if jurusan == "SBY" or jurusan == "sby":
    nama_jurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL" or jurusan == "bl":
    nama_jurusan = "Bali"
    harga = 350000
elif jurusan == "LMP" or jurusan == "lmp":
    nama_jurusan = "Lampung"
    harga = 500000
else: 
    nama_jurusan = "Salah kode"
    harga = 0

#proses penentuan potongan
if jummlah >= 3:
    potongan = (jummlah * harga) * 0.1
else:
    potongan = 0

#proses penjumlahan
total = harga * jummlah
jumlah_harga = total - potongan

#output cetak hasil
print("--------------------------------")
print("Penjualan tiket bus XYZ")
print("--------------------------------")
print("Nama pembeli : ",pembeli)
print("No HP : ",no_hp)
print("Kode Jurusan : ",jurusan)
print("Tujuan : ",nama_jurusan)
print("Harga : Rp ",harga)
print("Jumlah beli : ",jummlah)
print("--------------------------------")
print("Total : Rp ",total)
print("Potongan : Rp ",potongan)
print("Total Bayar : Rp ",jumlah_harga)

#proses pembayaran
bayar = int(input("Masukkan uang bayar : "))
kembali = bayar - jumlah_harga
print("Kembali : Rp ",kembali)

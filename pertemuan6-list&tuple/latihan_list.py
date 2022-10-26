n = int(input("Masukkan jumlah data : "))
nim = []
nama = []
nt1 = []
nt2 = []
nt = []

for i in range(n):
    nim.append(input("Masukkan NIM : "))
    nama.append(input("Masukkan Nama : "))
    nt1.append(int(input("Masukkan N.Tugas 1 : ")))
    nt2.append(int(input("Masukkan N.Tugas 2 : ")))
    print("=======================================")
    
    nt.append((nt1[i]+nt2[i])/2)

print("No | NIM | Nama | N. Tugas1 | N.Tugas2 | N.Tugas")
no = 1
for i in range(n):
    print(no, " | ", nim[i], " | ", nama[i], " | ", nt1[i], " | ", nt2[i], " | ", nt[i])
    no = no+1
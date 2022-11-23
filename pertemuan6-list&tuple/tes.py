nama = "amin"
nilai = 90
print("Nama = ",nama,"; nilai = ",nilai)
print("Nama = %s ;nilai = %i"%(nama,nilai))
# %s = string
# %i = int
# \t = tab

'''
#persiapan
nim = []
nama = []
nt1 = []
nt2 = []
nt = []

#input
n = int(input("Jml data : "))
print("=================================")

#proses
for i in range(n):
    nim.append(input("NIM : ")) 
    nama.append(input("Nama : ")) 
    nt1.append(int(input("N.Tugas 1 : "))) 
    nt2.append(int(2)) 
    
    nt.append((nt1[i]+nt2[i])/2)
    
    print("=================================")
       
#output
print("No | NIM | Nama | N. Tugas 1 | N. Tugas 2 | N. Tugas")
no = 1
for i in range(n):
    print(no," | ", nim[i]," | ", nama[i]," | ", nt1[i]," | ", nt2[i]," | ", nt[i])
    no = no+1
'''
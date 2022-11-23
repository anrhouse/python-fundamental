def sapa(nama):
    '''Yuk kenalan dengan fungsi'''
    return print("Selamat Siang " + nama)

def sapa2():
    return "Selamat Siang"

def tambah(a, b):
    c = a + b
    return c

def kali(a,b):
    c = (a * b) + tambah(a, b)
    return c

print(sapa('amin'),__doc__)
'''
hasil = tambah(4,6)
hasil = kali(hasil, hasil)
print(hasil)
'''

def grade(a):
    if a >= 50 :
        hasil = 'Lulus'
    else:
        hasil = 'Tidak Lulus'
    
    if a>= 70:
        ket = "Baik"
    elif a >= 50:
        ket = "Cukup"
    else:
        ket = "Jelek"
    
    c = [hasil, ket]
    
    return c

nilai = 80
hasil = grade(nilai)

print(hasil)
print("Nilai : ", nilai)
print('hasil : ', hasil[0])
print("Ket : ", hasil[1])








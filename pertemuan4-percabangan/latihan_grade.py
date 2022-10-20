print("Cara pertama")
print("================")
nilai = int(input("Masukkan Nilai : "))

if nilai >= 80 and nilai <= 100:
    grade = "A"
elif nilai >= 65 and nilai <= 79:
    grade = "B"
elif nilai >= 50 and nilai <= 64:
    grade = "C"
elif nilai >= 30 and nilai <= 49:
    grade = "D"
elif nilai <= 29 and nilai >= 0 :
    grade = "E"
else:
    grade ="Salah input"

print("Nilai : ", nilai)
print("Grade : ", grade)

print("================")
print("Cara Kedua")
print("================")
nilai = int(input("Masukkan Nilai : "))
#110
if nilai >= 80 and nilai <= 100:
    grade = "A"
elif nilai >= 65:
    grade = "B"
elif nilai >= 50:
    grade = "C"
elif nilai >= 30:
    grade = "D"
elif nilai <= 29 and nilai >= 0 :
    grade = "E"
else:
    grade ="Salah input"

print("Nilai : ", nilai)
print("Grade : ", grade)

print("================")
print("Cara Ketiga")
print("================")
nilai = int(input("Masukkan Nilai : "))

if nilai <= 29 and nilai >= 0: #0 - 100
    grade = "E"
elif nilai <= 49:
    grade = "D"
elif nilai <= 64:
    grade = "C"
elif nilai <= 79:
    grade = "B"
elif nilai <= 100 and nilai >= 80:
    grade = "A"
else:
    grade = "Salah input"

print("Nilai : ", nilai)
print("Grade : ", grade)
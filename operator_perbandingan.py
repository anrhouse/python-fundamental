nilai1 = 10
nilai2 = 9

lebihdari = nilai1 > nilai2
print(nilai1, " > ", nilai2, " = ", lebihdari)

kurangdari = nilai1 < nilai2
print(nilai1, " < ", nilai2, " = ", kurangdari)

lebihdari_samadengan = nilai1 >= nilai2
print(nilai1, " >= ", nilai2, " = ", lebihdari_samadengan)

kurangdari_samadengan = nilai1 <= nilai2
print(nilai1, " <= ", nilai2, " = ", kurangdari_samadengan)

samadengan = nilai1 == nilai2
print(nilai1, " == ", nilai2, " = ", samadengan)

tidaksamadengan = nilai1 != nilai2
print(nilai1, " != ", nilai2, " = ", tidaksamadengan)

logika_and = lebihdari and kurangdari
print(lebihdari, " and ", kurangdari, " = ", logika_and)

logika_or = lebihdari or kurangdari
print(lebihdari, " or ", kurangdari, " = ", logika_or)

logika_not = not logika_and
print("not ",logika_and, " = ", logika_not )

logika_not = not logika_or
print("not ",logika_or, " = ", logika_not )
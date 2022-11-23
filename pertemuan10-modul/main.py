import modul.aritmatika as n
from modul.perbandingan import *
from modul.logika import * 
from math import *

x = 3
y = 2

penjumlahan = n.penjumlahan(x,y)
pengurangan = n.pengurangan(x,y)
perkalihan = n.perkalihan(x,y)
pembagian = n.pembagian(x,y)
pangkat = n.pangkat(x,y)
pembagian_bulat = n.pembagian_bulat(x,y)
sisa_bagi = n.sisa_bagi(x,y)

print('x : ', x)
print('y : ', y)
print('x,y')
print('Penjumlahan : ',penjumlahan)
print('Pengurangan : ', pengurangan)
print('Perkalihan : ', perkalihan)
print('Pembagian : ', pembagian)
print('Pangkat : ', pangkat)
print('Pembagian Bulat : ', pembagian_bulat)
print('Sisa Bagi : ', sisa_bagi)
print('=======================================\n')


lebihdari = lebihdari(x,y)
kurangdari = kurangdari(x,y)
lebihdari_samadengan = lebihdari_samadengan(x,y)
kurangdari_samadengan = kurangdari_samadengan(x,y)
samadengan =samadengan(x,y)
tidak_samadengan = tidak_samadengan(x,y)

print('x : ', x)
print('y : ', y)
print('x,y')
print('lebih dari : ', lebihdari)
print('kurang dari : ', kurangdari)
print('lebih dari samadengan: ', lebihdari_samadengan)
print('kurang dari samadengan: ', kurangdari_samadengan)
print('samadengan: ', samadengan)
print('tidak samadengan: ', tidak_samadengan)
print('=======================================\n')

dan = dan(samadengan, lebihdari_samadengan)
atau = atau(samadengan, lebihdari_samadengan)
not_dan = tidak(dan)
not_atau = tidak(atau)

print('samadengan: ', samadengan)
print('lebih dari samadengan: ', lebihdari_samadengan)
print('samadengan, lebihdari_samadengan')
print('dan : ', dan)
print('atau : ', atau)
print('not dan : ', not_dan)
print('not atau : ', not_atau)
print('=======================================\n')

pow = pow(2,2)
factorial = factorial(3)
print('pow : ', pow)
print('factorial : ', factorial)
my_tupple = (1,2,3,[4,5,6],'a','b','c')
print(my_tupple)

#akses tupple yg isinya list
print(my_tupple[3])

#ubah list ke 0 menjadi 6, dan 2 menjadi 4 pada tupple ke 3
my_tupple[3][0] = 6
my_tupple[3][2] = 4
print(my_tupple[3])

#hapus isi list pada tupple
del(my_tupple[3][2])
print(my_tupple)
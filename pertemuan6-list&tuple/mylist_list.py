# list kosong
my_list = []
print(my_list)

#list dengan isi
my_list = [1,2,3,4,[5,[6.1,6.2,6.3],7,8],'a','b','c']
print(my_list)

#mengakses list (note : list dimulai dr 0)
print(my_list[0])
print(my_list[4])
print(my_list[4][0])
print(my_list[4][1])
print(my_list[4][1][1])
print(my_list[5])

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

#akss list dr beberapa anggota
print(my_list)
print(my_list[:3])
print(my_list[3:])
print(my_list[-3:])
print(my_list[-3:-1])
my_list = ['i','love','python','programming',2017]

#Menampilkan isi dari my_list
for i in range(len(my_list)):
    print(my_list[i])

your_list = ['hello',[1,2,3],'python']
#Menampilkan isi dari your
for i in range(len(your_list)):
    print(your_list[i])

#dengan list didalam list dipecah
for i in range(len(your_list)):
    print("List Asli : ",your_list[i])
    if len(your_list[i]) > 0:
        for n in range(len(your_list[i])):
            print(your_list[i][n])
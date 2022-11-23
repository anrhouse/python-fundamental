print("1. Buatlah persegi seperti berikut")
print("==================================")

no = 1
while no <= 3:
    n = 1
    while n <= 5:
        if n == 5:
            print("*")
        else:
            print("*",end='')
        n = n+1
    no = no+1
    
print("2. Buatlah segitiga seperti berikut")
print("==================================")

no = 1
while no <= 3:
    n = 1
    while n <= no:
        if n == no:
            print("*")
        else:
            print("*",end='')
        n = n+1
    no = no+1

print("3. Buatlah segitiga seperti berikut")
print("==================================")

no = 1
while no <= 3:
    n = 5
    while n >= 1:
        if n == 1:
            print("*")
        elif n <= no:
            print("*",end='')
        else:
            print(" ",end='')
        n = n-1
    no = no+1
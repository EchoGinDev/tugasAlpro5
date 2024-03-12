import os

def perkalian (a,b):
    for i in range(b):
        if i == b-1:
            print(str(b) + " = ")
        else:
            print(str(b) + " + ")
    print(str(a*b))

run = True
while (run):
    print("Perkalian")
    try:
        a = int(input("Angka Pertama : "))
        b = int(input("Angka Kedua : "))
        print("==============")
        c = perkalian(a,b)
        d = str(c).replace("/n", "")
        print( str(c).strip())
        os.system('cls')
    except:
        print("==============")
        print ("Jenis format salah")
        os.system('cls')


        
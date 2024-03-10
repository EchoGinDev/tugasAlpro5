def ganjil(bawah,atas):
    if bawah < atas :
        for i in range(bawah,atas):
            if i %2 == 1:
                print(i)
    elif bawah > atas :
        for i in range(bawah, atas, -1):
            if i %2 == 1:
                print(i) 

ganjil(30,10)
ganjil(97,82)
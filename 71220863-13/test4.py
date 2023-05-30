def jumlahdigit(n):
    nstr = str(n)
    total = 0
    for i in nstr:
        # print(i)
        total = total + int(i)
    return total
print(jumlahdigit(182771))

def jumlah_rekrusif(n):
    if n <10:
        return n 
    else:
        return n %10 + jumlah_rekrusif(n//10)    
print(jumlah_rekrusif(182771))
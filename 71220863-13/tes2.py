import timeit
def fibo(n):
    f1,f2=1,1
    # print(f1,", ",f2,", ",end='')
    for i in range(2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
        # print(fib,end=' ,')
    return fib



def fiborek(n):
    if n ==1 or n==2:
        return 1
    else:
        return fiborek(n-1)+fiborek(n-2)

def fibo_up(n,listfibo):
    if n ==1 or n==0:
        return 1
    else:
        if listfibo[n-1]!=0:
            return listfibo[n]
        else:
            listfibo[n-1]=fibo_up(n-1,listfibo)+fibo_up(n-2,listfibo)
            return fibo_up(n-1,listfibo)+fibo_up(n-2,listfibo)

n = 40
listfibo=[0]*n
start3= timeit.default_timer()
hasil = fibo_up(n, listfibo)
end3 = timeit.default_timer()
hasil3 = (end3-start3)

start = timeit.default_timer()
fibo(40)
end = timeit.default_timer()
waktu_perulangan = (end-start)        
        
start2= timeit.default_timer()
fiborek(40)
end2 = timeit.default_timer()
hasil2 = (end2-start2)



print(f'perulangan dengan waktu {waktu_perulangan} detik')
print(f'rekrusif upgrade dengan wktu {hasil3} detik')
print(f'rekrusif dengan waktu { hasil2} detik')

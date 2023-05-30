import sys
import timeit

sys.setrecursionlimit(5000)

def ulang(n):
    if n ==1:
        print('hello world rek',n)
        return
    else:
        print('hello world rek',n)
        ulang(n-1)

start = timeit.default_timer()
ulang(1000)
end = timeit.default_timer()
start2 = timeit.default_timer()
for i in range(1,1000):
    # pass
    print('hello world for ',i+1)
end2 = timeit.default_timer()
print(f'waktu yang di perlukan rekrusif : {((end-start)/1000)} milisecond')
print(f'waktu yang di perlukan perulangan : {((end2-start2)/1000)} milisecond')

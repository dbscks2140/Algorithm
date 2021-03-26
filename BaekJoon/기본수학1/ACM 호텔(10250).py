"""a = int(input())
b = int(input())
print(b + b - a)
import math
n = int(input())
t = 0
if n == 1:
    print(0)
    quit()
while True:
    if n % 2 == 0:
        if n == 1:
            break
        k = (n/2)**2
        t = t + k
        n = math.ceil(n / 2)

    else:
        if n <= 1:
            break
        k = (int(n/2)) * (int(n/2+1))
        t = t + k
        n = math.ceil(n / 2)

print(t)

"""
n = int(input())
t1 = list(map(int,input().split()))
t2 = list(map(int,input().split()))
f = 0

def sort(a,b):
    for j in range(n):
        for i in range(n-1):
            if a[i] < a[i+1]:
                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp

                tmp = b[i]
                b[i] = b[i + 1]
                b[i + 1] = tmp
def add(a,b):
    for i in range(n):
        a[i] =  a[i] + b[i]
for i in range(n):
        sort(t1,t2)
        f = f + t1[0]
        t1[0] = 0
        add(t1, t2)


print(f)









import math
def gcd(a, b):
    while(b != 0):
        tmp = a % b
        a = b
        b = tmp
    return a
n = int(input())
t = [' 'for _ in range(n)]
for i in range(n):
    t[i] = int(input())
t.sort(reverse=True)
k = t[0] - t[1]
for i in range(1,n-1):
    k = gcd(k,(t[i] - t[i+1]))
q = []
f = int(math.sqrt(k))
for i in range(2,f+1):
    if (k % i == 0):
        q.append(i)
        q.append(k//i)
q.append(k)
q = list(set(q))
q.sort()
for i in q:
    print(i, end=' ')




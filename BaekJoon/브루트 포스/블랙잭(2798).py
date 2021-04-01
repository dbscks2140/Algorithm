n, m = map(int,input().split())
t = list(map(int,input().split()))
s = 0
near = 0
k = 0
for i in range(0,n-2):
    s = 0
    s += t[i]
    for j in range(i+1,n-1):
        s += t[j]
        for r in range(j+1,n):
            s += t[r]
            if(s <= m and s > near):
                near = s
            s -= t[r]
            k += 1

        s -= t[j]
print(near)
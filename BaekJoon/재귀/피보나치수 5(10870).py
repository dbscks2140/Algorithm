n = int(input())
t = [0]*(n+2)
t[0] = 0
t[1] = 1
for i in range(2,n+2):
    t[i] = t[i-1] + t[i-2]
print(t[n])
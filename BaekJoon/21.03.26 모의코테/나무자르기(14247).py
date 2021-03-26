import sys
n = int(input())
t1 = list(map(int,sys.stdin.readline().split()))
t2 = list(map(int,sys.stdin.readline().split()))
t2.sort(reverse=True)
t = sum(t1)
for i in range(1,n):
    t = t + t2[i-1] * (n-i)
print(t)
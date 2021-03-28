import sys
n = int(input())
for i in range (n):
    a, b = map(int,input().split())
    A = list(map(int,sys.stdin.readline().split()))
    B = list(map(int,sys.stdin.readline().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    k = 0
    t = 0
    for x in range(a):
        for y in range(t,b):
            if(A[x] > B[y]):
                t = y
                k += b - y
                break
    print(k)
    k = 0

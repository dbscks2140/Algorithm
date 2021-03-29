def fac(n):     #재귀함수 정리 필요 !!
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)
n = int(input())
print(fac(n))



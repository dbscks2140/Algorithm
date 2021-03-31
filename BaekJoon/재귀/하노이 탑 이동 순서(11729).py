def hanoi(n, a, c, b):
    if n == 1:
        print(a, c)
        return
    hanoi(n - 1, a, b, c)   #n-1개의 원반을 a에서 b로 보조기둥은 c
    print(a ,c)
    hanoi(n - 1, b, c, a)   #n-1개의 원반을 b에서 c로 보조기둥은 a
n = int(input())
print(2**n - 1)
hanoi(n,1,3,2)



#www.youtube.com/watch?v=FYCGV6F1NuY 유튜브 영상 참조

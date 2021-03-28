for _ in range(int(input())):
    a = int(input())
    b = int(input())
    t = [[0]*(b)for _ in range(a+1)]

    for i in range(b):
        t[0][i] = i + 1

    for i in range(a+1):
        t[i][0] = 1

    for i in range(1,a+1):
        for j in range(1,b):
            t[i][j] = t[i-1][j] + t[i][j-1]
    print(t[a][b-1])
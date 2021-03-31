n = int(input())
s = [ [' 'for j in range(n)] for i in range(n)]
x = y = 0
def star(n,s,x,y):
    if n==1:
        s[x][y] = '*'
        return
    else:
        for i in range(3):
            for j in range(3):
                if (i==1 and j==1):
                    continue
                else:
                    star(n//3, s, x+i*n//3, y+j*n//3)
star(n,s,x,y)
for i in s:
    for j in i:
        print(j, end='')
    print()
w,h,n = map(int, input().split())
s_li = [[0]*w for _ in range(h)]

for i in range(n):
    x,y,q = map(int, input().split())
    for j in range(w):
        for k in range(h):
            if q == 1 and j < x:
                s_li[k][j] = 1
            elif q == 2 and j >= x:
                s_li[k][j] = 1
            elif q == 3 and k < y:
                s_li[k][j] = 1
            elif q == 4 and k >= y:
                s_li[k][j] = 1

ans = sum([sum(i == 0 for i in a)for a in s_li])

print(ans)

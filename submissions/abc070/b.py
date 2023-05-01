a,b,c,d = map(int, input().split())

upper = min(b,d)
lower = max(a,c)

print(max(0,upper-lower))

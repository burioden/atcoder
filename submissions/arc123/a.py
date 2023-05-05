a = list(map(int,input().split()))

x = a[1]*2 - a[0] - a[2]
k = max(0,(1-x)//2)

print(x+3*k)

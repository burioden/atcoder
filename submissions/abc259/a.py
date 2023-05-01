n,m,x,t,d = map(int, input().split())

if x<=m:
    print(t)
elif m==0:
    print(t-d*x)
else:
    print((t-d*x)+(d*m))

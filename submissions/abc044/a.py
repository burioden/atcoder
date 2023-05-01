a = [int(input()) for _ in range(4)]
n = a[0]
k = a[1]
x = a[2]
y = a[3]

if k>n:
    print(n*x)
else:
    print((k*x) + ((n-k)*y))

n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

b = []
ans = 0
for i in range(1,n):
    b.append(a[i-1] - a[i])
    ans += (a[0] - a[i])
nya = ans
for i in range(n-2):
    ans = (ans - ((b[i]) * (n-i-1)))
    nya += ans
    
print(nya)

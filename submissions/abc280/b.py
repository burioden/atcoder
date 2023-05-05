n = int(input())
a = list(map(int,input().split()))

b = [a[0]]
for i in range(1,n):
  b.append(a[i]-a[i-1])

print(*b)

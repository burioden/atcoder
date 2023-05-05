n = int(input())
a = list(map(int,input().split()))

x = 0

for i in range(n):
  x += 1/a[i]

print(1/x)

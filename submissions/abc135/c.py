n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

s = sum(a)

for i in range(n):
  if b[i] >= a[i]:
    tmp = b[i] - a[i]
    a[i] = 0
    if a[i+1] - tmp >= 0:
      a[i+1] -= tmp
    else:
      a[i+1] = 0
  else:
    a[i] -= b[i]

a[n] - tmp

print(s - sum(a))

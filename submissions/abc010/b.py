n = int(input())
a = list(map(int,input().split()))
aa = sum(a)

for i in range(n):
  if a[i]%6 == 0:
    a[i] -= 3
  elif (a[i]+1)%6 == 0:
    a[i] -= 2
  elif a[i]%2 == 0:
    a[i] -= 1

print(aa-sum(a))

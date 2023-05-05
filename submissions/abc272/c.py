n = int(input())
a = sorted(list(map(int,input().split())),reverse=1)

odd = []
even = []

for i in range(n):
  if a[i]%2 == 0:
    even.append(a[i])
  elif a[i]%2 == 1:
    odd.append(a[i])

o = 0
e = 0

ans = 0
if len(odd) < 2:
  if len(even) < 2:
    ans = -1
  else:
    e = even[0] + even[1]
elif len(even) < 2:
  o = odd[0] + odd[1]
else:
  e = even[0] + even[1]
  o = odd[0] + odd[1]
  
if ans != -1:
  ans = max(e,o)
  
print(ans)

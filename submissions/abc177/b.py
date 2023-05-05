s = input()
t = input()

n = len(s)
m = len(t)

cnt = n

for i in range(n-m+1):
  x = 0
  for j in range(m):
    if t[j] != s[i+j]:
      x += 1
  cnt = min(cnt,x)
  
print(cnt)

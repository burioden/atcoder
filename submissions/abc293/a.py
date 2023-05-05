s = list(input())
n = len(s)

for i in range(0, n - 1, 2):
  tmp = s[i]
  s[i] = s[i + 1]
  s[i + 1] = tmp
  
print(*s, sep='')

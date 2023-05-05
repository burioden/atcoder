s = list(input().split())
t = ['1','9','7','4']
n = len(s)

for i in s:
  if i in t:
    t.remove(i)
    
if len(t) == 0:
  print('YES')
else:
  print('NO')

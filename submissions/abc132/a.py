s = sorted(input())
n = len(set(s))
a = s[0]
b = s[-1]

if s.count(a) == 2 and s.count(b) == 2 and n == 2:
  print('Yes')
else:
  print('No')

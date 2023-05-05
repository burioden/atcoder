s = input()
n = len(s)

if s.count('hi') == n//2 and n%2 == 0:
  print('Yes')
else:
  print('No')

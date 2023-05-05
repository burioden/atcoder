n = int(input())
s = input()

a = s[:n//2]

if a+a == s:
  print('Yes')
else:
  print('No')

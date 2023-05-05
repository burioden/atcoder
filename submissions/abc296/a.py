n = int(input())
s = input()

if n == 1:
  exit(print('Yes'))

for i in range(1, n):
  if s[i - 1] == s[i]:
    exit(print('No'))
    
    
print('Yes')

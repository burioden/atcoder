n = int(input())
li = []
for i in range(n):
  s = input()
  li.append(s)

if len(set(li)) <= n-1:
  print('Yes')
else:
  print('No')

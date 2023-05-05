n = int(input())

for i in range(n):
  for j in range(n):
    if 4*i + 7*j == n:
      print('Yes')
      exit()

print('No')

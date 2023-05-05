n = int(input())

for i in range(1, 101):
  if n == i * i * i:
    exit(print('YES'))
    
print('NO')

n = int(input())

s = sorted('indeednow')

for _ in range(n):
  if sorted(input()) == s:
    print('YES')
  else:
    print('NO')
  

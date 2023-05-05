n,y = map(int,input().split())

ans = -1,-1,-1

for i in range(n+1):
  for j in range(n-i+1):
    z = n-i-j
    if y == (10000 * i) + (5000 * j) + (1000 * z) and 0<=z<=2000:
      ans = i,j,z
      break
  else:
      continue
  break

print(*ans)

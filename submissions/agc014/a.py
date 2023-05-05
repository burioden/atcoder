a,b,c = map(int, input().split())

if a==b==c and not a==1:
  print(-1)
  exit()

cnt = 0
for i in range(998244353):
  if a%2==1 or b%2==1 or c%2==1:
    break
  else:
    A,B,C = a,b,c
    A,B,C = A//2,B//2,C//2
    a,b,c = B+C,A+C,A+B
    cnt += 1

print(cnt)

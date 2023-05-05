n = int(input())
a = sorted(list(map(int,input().split())))

ans = a[0]
if ans == 0:
  print(0)
  exit()
  
for i in range(1,n):
  ans *= a[i]
  if ans > 10**18:
    print(-1)
    exit()
    
print(ans)

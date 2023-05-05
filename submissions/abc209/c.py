n = int(input())
c = sorted(list(map(int,input().split())))

ans = 1
for i in range(n):
  if c[i]-i < 0:
    print(0)
    exit()
  else:
    ans *= (c[i]-i)
    ans %= 1000000007
    
print(ans)

n,k,m = map(int,input().split())
a = list(map(int,input().split()))

for x in range(k+1):
  if (sum(a) + x)/n >= m:
    print(x)
    exit()

print(-1)

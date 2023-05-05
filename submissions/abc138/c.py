n = int(input())
v = sorted(list(map(int,input().split())))

for i in range(1,n):
  x = (v[i-1]+v[i])/2
  v[i] = x

print(v[-1])

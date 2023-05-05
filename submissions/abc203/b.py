n,k = map(int,input().split())

li = []

for i in range(1,n+1):
  for l in range(1,k+1):
    li.append(i*100+l)

print(sum(li))

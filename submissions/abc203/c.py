n,k = map(int,input().split())
li = sorted([list(map(int, input().split())) for _ in range(n)])

for i in li:
  if i[0] <= k:
    k += i[1]

print(k)

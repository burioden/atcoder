a,b = map(int, input().split())
li =[]
ans = []

for i in range(a,b+1):
  li.append(str(i))


for i in range(len(li)):
  inner = 0
  for l in range(5):
    if li[i][l] == li[i][(5-1)-l]:
      inner += 1
  ans.append(inner)

print(ans.count(5))

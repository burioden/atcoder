n = int(input())

li = [2,1]
inner = 0

for i in range(1,n):
  inner = li[i-1]+li[i]
  li.append(inner)

print(li[n])

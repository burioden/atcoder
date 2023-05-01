n = int(input())
li = list(map(int, input().split()))

li2 = sorted(li)

a = 0
b = 0

for i in range(0,len(li2),2):
  a += li2[i]
for i in range(1,len(li2),2):
  b += li2[i]

print(abs(a-b))

n = int(input())
s = input()

x = 0
li = []
li2 = [0]

for i in range(n):
  if s[i] == "I":
    li.append(1)
  else:
    li.append(-1)

for i in range(n):
  x += li[i]
  li2.append(x)
  
print(max(li2))

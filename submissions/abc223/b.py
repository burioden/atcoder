s = list(input())
li = [[] for i in range(len(s))]

for i in range(len(s)):
  x = s.pop()
  li[i] = [x]+s
  s = [x]+s

print(*min(li),sep="")
print(*max(li),sep="")

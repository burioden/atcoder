n = int(input())
s = input()
k = int(input())

li = []

z = s[k-1]

for i in range(n):
  if s[i] != z:
    li.append("*")
  else:
    li.append(s[i])

print(''.join(map(str, li)))

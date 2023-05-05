from os import remove


s = input()
a = "aiueo"
li = []
for i in s:
  if i not in a:
    li.append(i)

print(*li,sep="")

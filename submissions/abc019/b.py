s = list(input())
i = 0

while i < len(s):
  j = i
  while j < len(s) and s[i] == s[j]:
    j += 1
  print(s[i]+str(j-i),end="")
  i = j

print("")

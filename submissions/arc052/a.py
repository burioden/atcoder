s = input()

ans = []

for i in s:
  if i.isdigit():
    ans.append(i)
    
print(*ans, sep='')

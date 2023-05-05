s = input()
n = int(input())

ans = set()
if len(s) < n:
  print(0)
  exit()

for i in range(len(s)-n+1):
  ans.add(s[i:i+n])

print(len(ans))

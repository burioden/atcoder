n = int(input())

poem = set()
ans = []

for i in range(n):
  s, t = input().split()
  t = int(t) * -1
  if s not in poem:
    poem.add(s)
    ans.append([t, i + 1])
    
ans.sort()

print(ans[0][1])

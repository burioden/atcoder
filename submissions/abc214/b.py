s,t = map(int, input().split())

x = max(s,t) + 1
cnt = 0
for i in range(x):
  for j in range(x):
    for k in range(x):
      if i + j + k > s or i * j * k > t:
        break
      elif i + j + k <= s:
        if i * j * k <= t:
          cnt += 1
      
print(cnt)

n = int(input())

cnt = 0

for i in range(1, n + 1):
  for j in range(1, n + 1):
    for k in range(1, n + 1):
      cnt += 1
      
print(cnt)

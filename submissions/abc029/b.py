li = [input() for _ in range(12)]

cnt = 0

for i in li:
  if "r" in i:
    cnt += 1

print(cnt)

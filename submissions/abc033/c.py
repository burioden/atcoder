s = input().split("+")
cnt = 0
for i in s:
  if "0" not in i:
    cnt += 1

print(cnt)

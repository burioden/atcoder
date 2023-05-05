li = [list(input().split()[::-1]) for _ in range(4)][::-1]

for i in range(4):
  print(*li[i])

li = sorted(list(map(int, input().split())))
k = int(input())

ans = 0

for i in range(k):
  li[2] *= 2

print(sum(li))

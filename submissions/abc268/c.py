n = int(input())
p = list(map(int,input().split()))

h = [0]*n

for i in range(n):
  for j in range(3):
    x = (p[i] - i - j + 1) % n
    h[x] += 1

print(max(h))

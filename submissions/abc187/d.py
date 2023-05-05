n = int(input())
Takahashi = 0
Aoki = 0
c = []
for i in range(n):
  a,b = map(int,input().split())
  Aoki += a
  # Takahashi += b
  c.append([2*a+b,a,b])

c.sort(reverse=1)

cnt = 0
i = 0

while Takahashi <= Aoki:
  Aoki -= c[i][1]
  Takahashi += c[i][1]+c[i][2]
  i += 1
  cnt += 1

print(cnt)

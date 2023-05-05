n = int(input())
h = list(map(int,input().split()))

top = 0

for i in range(1,n):
  if h[i-1] < h[i]:
    top = h[i]
  else:
    print(h[i-1])
    exit()

print(top)

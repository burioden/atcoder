n = int(input())
a = list(map(int,input().split()))

ans = 1
max_a = a[0]

for i in range(1,n):
  if a[i-1] <= a[i] and max_a <= a[i]:
    max_a = a[i]
    ans += 1

print(ans)

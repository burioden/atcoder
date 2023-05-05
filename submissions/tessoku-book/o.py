import bisect

n = int(input())
a = list(map(int,input().split()))

b = [0]*n
aa = sorted(set(a))

for i in range(n):
  b[i] = bisect.bisect_left(aa,a[i]+1)

print(*b)

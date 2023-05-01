#!/usr/bin/env python3
n,a,b = map(int, input().split())
ans = 0

for i in range(1,n+1):
  if a <= sum(map(int, str(i))) <= b:
    ans += i

print(ans)

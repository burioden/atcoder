from itertools import combinations
n = int(input())
l = list(map(int,input().split()))

ans = 0

for a,b,c in combinations(l,3):
  if a != b and b != c and c != a:
    if abs(b-c)<a<b+c:
      ans += 1

print(ans)

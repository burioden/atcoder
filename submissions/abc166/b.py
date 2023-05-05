n, k = map(int, input().split())
sunuke = set()
for i in range(k):
  d = int(input())
  a = list(map(int, input().split()))
  for j in range(d):
    sunuke.add(a[j])
    
print(n - len(sunuke))

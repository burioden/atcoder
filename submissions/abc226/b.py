n = int(input())
s = set()
for i in range(n):
  a = list(map(int, input().split()))
  a = tuple(a)
  s.add(a)
  
print(len(s))

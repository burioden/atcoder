import itertools

n = int(input())
a = sorted(list(map(int,input().split())),reverse=1)

b = [a[0],a[1],a[2]]

c = []
for i in itertools.permutations(b,3):
  x = ''.join([str(n) for n in i])
  c.append(int(x))
  
print(max(c))

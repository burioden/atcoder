n = int(input())
a = [input() for _ in range(3)]

a = zip(*a)

cnt = 0
for i in a:
  x = len(set(i))
  if x > 1:
    cnt += (x-1)
    
print(cnt)

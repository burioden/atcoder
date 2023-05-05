h,w = map(int,input().split())
futon = []
for i in range(h):
  s = input()
  futon.append(s)
  
cnt = 0
for i in futon:
  for j in range(1,w):
    if i[j-1] == '.' and i[j] == '.':
      cnt += 1
      
futon = zip(*futon)

for i in futon:
  for j in range(1,h):
    if i[j-1] == '.' and i[j] == '.':
      cnt += 1
      
print(cnt)

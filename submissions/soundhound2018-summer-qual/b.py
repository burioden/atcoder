s = input()
w = int(input())

nya = []

for i,d in enumerate(s):
  if i%w == 0:
    nya.append(d)
    
print(*nya,sep='')

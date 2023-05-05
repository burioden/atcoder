s = input()

if s[0] == "1":
  print("No")
  exit()

p = [[int(s[6])],[int(s[3])],[int(s[1]),int(s[7])],[int(s[0]),int(s[4])],[int(s[2]),int(s[8])],[int(s[5])],[int(s[9])]]

a = []

for i,d in enumerate(p):
  if sum(d) > 0:
    a.append(i)

for i in range(1,len(a)):
  if a[i-1]+1 != a[i]:
    print('Yes')
    exit()

print('No')

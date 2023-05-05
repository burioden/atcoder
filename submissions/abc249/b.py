s = input()

p = len(set(s))
x = len(s)

li = []

for i in range(x):
  li.append(ord(s[i]))

li = sorted(li)

if p == x and li[0] <= 96 and 97 <= li[-1]:
  print('Yes')
else:
  print('No')

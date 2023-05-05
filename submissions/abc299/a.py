n = int(input())
s = input()

a = []
b = 0

for i, d in enumerate(s):
  if d == '|':
    a.append(i)
  if d == '*':
    b = i
    
print('in' if a[0] < b < a[1] else 'out')

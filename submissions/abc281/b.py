s = input()

f = s[0]
e = s[-1]
n = len(s)
m = s[1:-1]

if m.isdigit() is False:
  print('No')
  exit()

if n == 8:
  if f.isupper():
    if e.isupper():
     if 100000 <= int(m) <= 999999:
        print('Yes')
        exit()

print('No')

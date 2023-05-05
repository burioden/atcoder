s = input()
S = len(s)

for i in s:
  s = s[:-1]
  if len(s) % 2 == 0:
    if s == s[:(len(s)//2)] * 2:
      print(len(s))
      break

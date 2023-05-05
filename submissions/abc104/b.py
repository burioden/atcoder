s = input()

flg = 1

if s[0] != "A":
  flg = 0
elif "C" not in s[2:-1]:
  flg = 0
elif s.count("C") > 1:
  flg = 0
elif len(s)-2 != sum(map(str.islower,s)):
  flg = 0

print('AC' if flg else 'WA')

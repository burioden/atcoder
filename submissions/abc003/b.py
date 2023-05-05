s = list(input())
t = list(input())
a = list("atcoder")

# まず、Sについて
if s != t and "@" in s:
  for i,d in enumerate(s):
    if d == "@" and s[i] != t[i]:
      if t[i] in a:
        s[i] = t[i]

if s != t and "@" in t:
  for ii,dd in enumerate(t):
    if dd == "@" and s[ii] != t[ii]:
      if s[ii] in a:
        t[ii] = s[ii]

print("You can win" if s==t else "You will lose")

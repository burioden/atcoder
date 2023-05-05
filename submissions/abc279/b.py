s = input()
t = input()

S = len(s)
T = len(t)

flg = 0
for i in range(S-T+1):
  if s[i:i+T] == t:
    flg = 1
    break
# if s == t:
  # flg = 1

print('Yes' if flg else 'No')

# if t in s:
#   print('Yes')
# else:
#   print('No')

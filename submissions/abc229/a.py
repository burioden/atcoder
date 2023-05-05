s = input()
s1 = input()

S = s+s1

flg = 1

if S == '#..#' or S == '.##.':
  flg = 0
elif S.count('#') <= 1:
  flg = 0

print('Yes' if flg else 'No')

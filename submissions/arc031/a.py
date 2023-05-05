s = input()
def f(s):
    n = len(s)
    flg = True
    for i in range(n):
        if s[i] != s[(n-1)-i]:
            flg = False
            break
    return flg
  
if f(s):
  print('YES')
else:
  print('NO')

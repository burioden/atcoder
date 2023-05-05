def f(s):
    n = len(s)
    flg = True
    for i in range(n):
        if s[i] != s[(n-1)-i]:
          if s[i] == '*' or s[(n - 1) - i] == '*':
            continue
          flg = False
          break
    return flg
  
print('YES' if f(input()) else 'NO')

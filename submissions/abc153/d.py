def f(n):
    cnt = 1
    while 0 < n:
      n //= 2
      cnt *= 2
    return cnt

print(f(int(input()))-1)

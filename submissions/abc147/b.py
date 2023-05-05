s = input()

def f(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        if s[i] != s[(n-1)-i]:
            cnt += 1
    return cnt
  
print(f(s)//2)

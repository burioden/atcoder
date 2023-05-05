n = int(input())
n = ((n + 1) * n) // 2

def f(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print('WANWAN' if f(n) else 'BOWWOW')

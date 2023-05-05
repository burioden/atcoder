n = int(input())
a = list(map(int,input().split()))

def f(n):
    cnt = 0
    while n%2 == 0:
        n //= 2
        cnt += 1
    return cnt

ans = 0
for i in a:
  ans += f(i)

print(ans)

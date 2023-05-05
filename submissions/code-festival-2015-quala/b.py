'''
(a[0] * 2 ^ n) + (a[1] * 2 ^ n - 1) + (a[2] * 2 ^ n - 2)...
'''

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
  ans += (a[i] * (2 ** (n - i)))
  
print(ans // 2)

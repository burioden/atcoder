a, b, c = map(int, input().split())

mod = 998244353
ans = (a * (a + 1)) * (b * (b + 1)) * (c * (c + 1)) // 8 % mod

print(ans)

n = int(input())
a = list(map(int,input().split()))

MOD = 1000000007
s = sum(a)
t = sum(map(lambda x : x*x ,a))

print((s*s-t)//2 % MOD)

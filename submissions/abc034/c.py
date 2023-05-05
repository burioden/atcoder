import math

w,h = map(int,input().split())
MOD = 1000000007
print((math.factorial((w-1)+(h-1)) // (math.factorial(w-1) * math.factorial(h-1))) % MOD)

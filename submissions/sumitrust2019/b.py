import math

n = int(input())

x = math.ceil(n/1.08)

print(x if math.floor(x*1.08)==n else ':(')

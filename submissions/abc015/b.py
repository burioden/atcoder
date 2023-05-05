import math

n = int(input())
a = list(map(int,input().split()))

c = a.count(0)

print(math.ceil(sum(a)/(n-c)))

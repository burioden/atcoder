'''
2..nの最小公倍数+1？
'''

import math
import functools

n = int(input())

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*integers):
    return functools.reduce(my_lcm_base, integers)

b = []
for i in range(2,n+1):
    b.append(i)
    
print(lcm(*b)+1)

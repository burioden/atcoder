from decimal import Decimal, getcontext
getcontext().prec = 100
a,b = map(Decimal,input().split())

print(int(a*b))

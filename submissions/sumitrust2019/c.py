x = int(input())

y = x//100
k = x-(100*y)

print(1 if k <= y*5 else 0)

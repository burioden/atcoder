n = int(input()) + 1

a, b = 0, 1
li = []
while n:
  n -= 1
  li.append(b)
  a, b = b, a + b
  
print(li[-1])

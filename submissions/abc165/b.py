x = int(input())

sum = 100
y = 0

while sum < x:
  sum += sum//100
  y += 1

print(y)

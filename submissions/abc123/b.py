a = [int(input()) for _ in range(5)]
b = []

max = 0

for i in a:
  if i%10 != 0:
    if max < 10-(i%10):
      max = 10-(i%10)
      b.append(i+10-(i%10))
    else:
      b.append(i+10-(i%10))
  else:
    b.append(i)

print(sum(b)-max)

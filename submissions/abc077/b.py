n = int(input())

for i in range(1,40101):
  if i*i == n:
    print(n)
    break
  else:
    if i*i > n:
      print((i-1)*(i-1))
      break

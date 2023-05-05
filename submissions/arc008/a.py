n = int(input())

if n % 10 >= 7:
  print((n // 10 + (n % 10 > 0)) * 100)
else:
  print((n // 10) * 100 + (n % 10 * 15))

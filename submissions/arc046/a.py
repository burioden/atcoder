n = int(input())

if n < 10:
  print(n)
else:
  cnt = 9
  for i in range(11, 555556):
    if len(set(str(i))) == 1:
      cnt += 1
      if cnt == n:
        exit(print(i))

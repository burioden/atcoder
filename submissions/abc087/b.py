a,b,c,d = [int(input()) for i in range(4)]

cnt = 0

for A in range(a+1):
  for B in range(b+1):
    for C in range(c+1):
      if (500*A) + (100*B) + (50*C) == d:
        cnt += 1

print(cnt)

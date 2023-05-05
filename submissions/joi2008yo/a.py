n = int(input())

yen = 1000 - n
cnt = 0
coin = 500

while yen > 0:
  if coin <= yen:
    yen -= coin
    cnt += 1
  else:
    if coin == 500:
      coin = 100
    elif coin == 100:
      coin = 50
    elif coin == 50:
      coin = 10
    elif coin == 10:
      coin = 5
    else:
      coin = 1

print(cnt)

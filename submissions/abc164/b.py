a,b,c,d = map(int, input().split())

flg = 1

while 0 < a:
  c = c-b
  if 0 < c:
    a = a-d
    if 0 >= a:
      flg = 0
      break
  else:break

print("Yes" if flg else "No")

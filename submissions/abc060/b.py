a,b,c = map(int, input().split())

flg = 0

for i in range(1,101):
  if ((b*i)+c)%a == 0:
    flg = 1
    break

print("YES" if flg else "NO")

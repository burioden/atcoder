n = int(input())

ans = ""
x = n*1.08//1

if x > 206:
  ans = ":("
elif x == 206:
  ans = "so-so"
else:
  ans = "Yay!"

print(ans)

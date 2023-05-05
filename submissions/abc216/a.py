x,y = map(int, input().split("."))

s = ""

if y >= 7:
  s = "+"
elif y >= 3:
  s = ""
else:
  s = "-"

print(str(x)+s)

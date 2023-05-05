a,b,c = map(int, input().split())

ans = ""

if c%2 == 1:
  if a < b:
    print("<")
  elif a > b:
    print(">")
  else:
    print("=")
else:
  a = abs(a)
  b = abs(b)
  if a > b:
    print(">")
  elif a < b:
    print("<")
  else:
    print("=")

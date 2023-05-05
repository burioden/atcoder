n = int(input())
s = input()
S = "b"

for i in range(n):
  if s == S:
    print(i)
    exit()
  elif i%3 == 1:
    S = "c" + S + "a"
  elif i%3 == 0:
    S = "a" + S + "c"
  else:
    S = "b" + S +"b"

print(-1)

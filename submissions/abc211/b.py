b = ["H" , "2B" , "3B" , "HR"]

for i in range(4):
  s = input()
  if s in b:
    b.remove(s)

print("Yes" if len(b) == 0 else "No")

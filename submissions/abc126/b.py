s = input()

A = int(s[0])*10 + int(s[1])
B = int(s[2])*10 + int(s[3])

if 1 <= A <= 12:
  if 1 <= B <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
elif 1 <= B <= 12:
  print("YYMM")
else:
  print("NA")

a = [int(input()) for i in range(6)]

flag = 1

for i in range(5):
  for j in range(i+1,5):
    if a[j] - a[i] > a[5]:
      flag = 0
      break

print("Yay!" if flag else ":(")

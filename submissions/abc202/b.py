li = list(map(int,input()))[::-1]

for i in range(len(li)):
  if li[i] == 6:
    li[i] = 9
  elif li[i] == 9:
    li[i] = 6

print(''.join(map(str, li)))

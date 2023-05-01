n = int(input())
li = sorted(list(map(int, input().split())))

if li[n-1] < sum(li)-li[n-1]:
  print("Yes")
else:
  print("No")

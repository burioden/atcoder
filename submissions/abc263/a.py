list = list(map(int, input().split()))

c1 = list.count(list[0])
c2 = list.count(list[1])
c3 = list.count(list[2])
c4 = list.count(list[3])
c5 = list.count(list[4])

if c1 == 3 or c2 == 3 or c3 == 3 or c4 == 3 or c5 == 3:
	if c1 == 2 or c2 == 2 or c3 == 2 or c4 == 2 or c5 == 2:
		print("Yes")
	else:print("No")
else:print("No")

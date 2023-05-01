n = int(input())
a = [input() for _ in range(n)]

ck = 1

for i in range(n):
	for j in range(n):
		if a[i][j]=="W" and a[j][i]!="L":
			ck = 0
		elif a[i][j]=="D" and a[j][i]!="D":
			ck = 0
		elif a[i][j]=="L" and a[j][i]!="W":
			ck = 0

if ck:
	print("correct")
else:
	print("incorrect")

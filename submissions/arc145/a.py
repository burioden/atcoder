n = int(input())
s = input()

if s[0] == "A" and s[-1] == "B":
	print("No")
elif s == "BA":
	print("No")
else:
	print("Yes")

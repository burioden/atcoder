s = input()
rs = s[::-1]

start = s.index("A")+1
end = len(s)-rs.index("Z")+1

print(end-start)

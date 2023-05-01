s = sorted(input())
ss = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

ans = set(s) ^ set(ss)

print(" ".join(map(str, ans)))

a = list(map(int, input().split()))

print("win" if sum(a) < 22 else "bust")

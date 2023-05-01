s = input()
ns = "".join(map(str, sorted(s)))

print("Yes" if ns=="abc" else "No")

li = [input() for _ in range(3)]
il = ["ARC","AGC","AHC","ABC"]

ans = set(il) ^ set(li)

print(''.join(map(str, ans)))

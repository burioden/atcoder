n = int(input())
li = [input() for _ in range(n)]

print("AC","x",li.count("AC"))
print("WA","x",li.count("WA"))
print("TLE","x",li.count("TLE"))
print("RE","x",li.count("RE"))

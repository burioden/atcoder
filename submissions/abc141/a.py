s = input()
tenki = ["Sunny", "Cloudy", "Rainy"]
x = (tenki.index(s) + 1) % 3

print(tenki[x])

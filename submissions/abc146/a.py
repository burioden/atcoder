s = input()
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

n = week.index(s)

print(7 - n if n != 0 else 7)

x = int(input())

ultra_happy = (x//500) * 1000
happy = (x - ((x//500)*500)) // 5 * 5

print(ultra_happy+happy)

a = list(input())
b = list(input())
c = list(input())

now = "a"

while 1:
    if now == "a":
        if a:
            now = a.pop(0)
        else:
            print("A")
            break
    elif now == "b":
        if b:
            now = b.pop(0)
        else:
            print("B")
            break
    else:
        if c:
            now = c.pop(0)
        else:
            print("C")
            break

x = input()
x = x.replace("ch","").replace("o","").replace("k","").replace("u","")
print("YES" if len(x)==0 else "NO")

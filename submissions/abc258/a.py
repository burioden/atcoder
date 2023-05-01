k = int(input())

hh = round(k//60)+21
m = str(k%60)

mm = m.zfill(2)

print(str(hh) + ":" + mm)

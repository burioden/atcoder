import string

s = list(input())
alp = list(string.ascii_lowercase)

dif_li = sorted(list(set(s) ^ set(alp)))

print(dif_li[0] if len(dif_li) > 0 else "None")

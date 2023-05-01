l,r = map(int, input().split())
s = list(input())
li = s[l-1:r]
li_start = s[:l-1]
li_end= s[r:]
li = li[::-1]

print("".join(li_start + li + li_end))

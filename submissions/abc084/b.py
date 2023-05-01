#!/usr/bin/env python3
a,b = map(int, input().split())
s = input()

flg = 1

if len(s) != (a+b+1):
  flg = 0
elif s[a] != "-":
  flg = 0
elif s.count("-") != 1:
  flg = 0

print("Yes" if flg else "No")

n = list(map(int,input()))
a = n[0]
b = n[1]
c = n[2]
d = n[3]

if a+b+c+d == 7:
  op = ["+","+","+"]
elif a+b+c-d == 7:
  op = ["+","+","-"]
elif a+b-c+d == 7:
  op = ["+","-","+"]
elif a+b-c-d == 7:
  op = ["+","-","-"]
elif a-b+c+d == 7:
  op = ["-","+","+"]
elif a-b+c-d == 7:
  op = ["-","+","-"]
elif a-b-c+d == 7:
  op = ["-","-","+"]
elif a-b-c-d == 7:
  op = ["-","-","-"]

print(a,op[0],b,op[1],c,op[2],d,"=7",sep="")

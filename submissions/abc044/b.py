w = list(input())

flag = True

for i in range(len(w)):
    #print(str(w[i]) + ":" + str(i) +"番目の字")
    #print(str(w.count(w[i])) + "回出てくる")
    #例：w[1]="a"なので、aの出現回数をカウントできる
    
    if w.count(w[i])%2 == 1:
        flag = False

if flag:
    print("Yes")
else:
    print("No")

import functools

# 最小公倍数
# https://ictsr4.com/py/m0150.html
def lcm(a, b):
    r = a % b
    if r == 0:
        return a
    return a * lcm(b, r) // r
  
n, m = map(int, input().split())
a = list(map(int,input().split()))

# 公倍数の半分、ということは、最初に半分にしたものたちの公倍数を求めればよい
c = [i//2 for i in a]

# x = aを半分にした配列cの最小公倍数
x = functools.reduce(lcm, c)

# y = kまでの間にxはいつくあるか
# 個数だけみればよいので、シミュレーションは不要
y = m // x

# cの中に、最小公倍数と割った結果が偶数になるものがあったら、半公倍数は叶わないため0を出力し終了
for i in c:
  if (x//i) % 2 == 0:
    print(0)
    exit()

# 元の数列aの最小公倍数と重複しているものは、0.5をかけても公倍数とならないため半分に？ちょっと自信ない
ans = (y+1)//2

print(ans)


# ダメだったコード

# def lcm(list_l):
#     greatest = max(list_l)
#     i = 1
#     while True:
#         for j in list_l:
#             if (greatest * i) % j != 0:
#                 i += 1
#                 break
#         else:
#             return greatest * i

# x = lcm(a)
# cnt = 0

# 最小公倍数を列挙していって、元の公倍数と割り切れなかったらプラスをしたかったけれど
# 偶数の存在を忘れていたナリ
# for i in range(1,m*2+1,x):
#   if (i*x)//2 % x != 0:
#     cnt += 1
  
# print(cnt//2)

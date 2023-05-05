import datetime

a,b,c,d,e = map(int, input().split())

okiru = datetime.datetime(2022,12,31,a,b)
ganbaru = okiru + datetime.timedelta(minutes=e)
neru =  datetime.datetime(2022,12,31,c,d)
yareru = neru - ganbaru

print(int(yareru.total_seconds()//60))

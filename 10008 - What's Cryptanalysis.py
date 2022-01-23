import collections
data=str()
for t in range(int(input())):
    t1=input().upper()
    data+=t1
didi={t2:data.count(t2) for t2 in data if t2.isalpha()}
b = sorted(didi.items(), key = lambda d:d[1], reverse = True)
for f,s in b:print(f"{f} {s}")
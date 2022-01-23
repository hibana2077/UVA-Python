from collections import Counter
co=Counter()
for t in range(int(input())):co+=Counter(input().upper())
for f,s in [(k,a) for k,a in list(co.most_common(len(co))) if str(k).isalpha()]:print(f,s)

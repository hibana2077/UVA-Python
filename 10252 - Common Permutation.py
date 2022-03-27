from collections import Counter
while True:
    try:
        a=Counter(set(input()))
        b=Counter(set(input()))
        for t in sorted([f for f,s in list(Counter(a+b).most_common(len(a)+len(b))) if s>=2]):print(t,end='')
    except EOFError:break

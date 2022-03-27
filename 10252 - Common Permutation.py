from collections import Counter
while True:
    try:for t in sorted([f for f,s in list(Counter(Counter(set(input()))+Counter(set(input()))).most_common(len(a)+len(b))) if s>=2]):print(t,end='')
    except EOFError:break

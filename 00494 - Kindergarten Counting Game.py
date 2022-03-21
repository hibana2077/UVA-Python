import sys,itertools
for line in sys.stdin:print(len(list(k for k,t in itertools.groupby(line,str.isalpha)if k==True)))
'''
偏醜
'''
outtype=["Wrong Answer","Output Format Error","Yes",lambda x,y:list(x)==list(y),lambda x,y:''.join(x.split())==''.join(y.split())]
for t in range(int(input())):temp=[input(),input()];print(f"Case {t+1}: {outtype[outtype[3](temp[0],temp[1])+outtype[4](temp[0],temp[1])]}")
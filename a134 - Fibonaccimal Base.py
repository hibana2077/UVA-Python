#a134 fibonacci base
a = [0,1]
for t in range(2,45+1):a.append(a[t-1]+a[t-2])
a = a[2::][::-1]

def solve(a,num):
    ans,flag = "",False
    for i in a:
        if num >= i:
            num -= i
            ans+="1"
            flag = True
        elif flag == True:ans+="0"
    return ans

for t in range(int(input())):
    num = int(input())
    print(f"{num} = {solve(a,num)} (fib)")
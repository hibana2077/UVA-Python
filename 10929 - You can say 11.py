'''
Author: your name
Date: 2022-03-23 10:06:08
LastEditTime: 2022-03-23 10:12:42
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \程式\python\10929 - You can say 11.py
'''
while True:
    a=int(input())
    if a>0:print(f"{a} is a multiple of 11.") if a%11==0 else print(f"{a} is not a multiple of 11.")
    else:break
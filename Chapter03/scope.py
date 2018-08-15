# -*- coding: utf-8 -*-

# 全局变量
balance = 1

def change():
    # 定义全局变量
    global balance
    balance = 100
    # 局部变量
    num = 20
    print("change() balance={0}".format(balance) )

if __name__ == "__main__" :
    change()
    print("修改后的 balance={0}".format(balance) )







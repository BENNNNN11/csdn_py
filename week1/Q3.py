#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-23 03:07
# @Author : XXX
# @Site : 
# @File : Q3.py
# @Software: PyCharm
import pandas as pd
import sys
'''
    自动取款机
    1. 登录
    2. 查询余额
    3. 取钱
    4. 存钱
    5. 退出系统
    6. 界面和交互
'''

# 1. User Details
user_info = \
    [{"name":"张三","balance":10000,"password":"000000","card_number":"0000000000000000000"},
{"name":"李四","balance":20000,"password":"111111","card_number":"1111111111111111111"},
{"name":"王五","balance":30000,"password":"222222","card_number":"2222222222222222222"}]

df = pd.DataFrame(user_info, columns=['name', 'balance', 'password', 'card_number'])

# 2. 登录

def Log_on(account):
    if account not in list(df['card_number']):
        print('银行卡无效，请取卡。')
        sys.exit()

    chance = 0
    log_on = True
    while log_on:
        passward = input('请输入密码：')
        for item in user_info:
            if item['card_number'] == account:
                if item['password'] == passward:
                    print('登录成功')
                    log_on = False
                    break
                else:
                    print("密码错误，请重新输入")
                    chance += 1
                    if (chance == 3):
                        print("三次密码输入失败，登录失败")
                        log_on = False
                        break


# 2. 查询余额
def balance(account):
    for item in user_info:
        if item['card_number'] == account:
            fund = item['balance']
            print('您的余额是： {}'.format(fund))

# 3. 存钱
def deposit(account):
    deposit_money = input("请输入您要存款的金额： ")
    for item in user_info:
        if item['card_number'] == account:
            item['balance'] += int(deposit_money)
            print("存款成功")
            print('您的余额是： {}'.format(item['balance']))

# 4. 取钱
def withdraw(account):
    withdraw_money = input("请输入您要取款的金额： ")
    for item in user_info:
        if item['card_number'] == account:
            if item['balance'] >= int(withdraw_money):
                item['balance'] -= int(withdraw_money)
                print("取款成功")
                print('您的余额是： {}'.format(item['balance']))
            else:
                print("余额不足，取款失败")

# 6. 退出系统
def logOut():
    pass


# 7. 界面和交互
print('='*12, '欢迎使用自动取款机', '='*12)  # 输出初始界面
account = input('请输入银行卡号：')
Log_on(account)
while True:
    print('{:1} {:<13} {:<15}'.format(' ', '1. 查看余额', '2. 存款'))
    print('{:1} {:<13} {:<15}'.format(' ', '3. 取款', '4. 退出系统'))
    print('='*40)
    key = input("请输入对应的选择： ")
    if key == '1':
        print("=" * 12, "银行卡余额", "="*12)
        balance(account)
        input("按回车继续： ")
    elif key == '2':
        print("=" * 12, "存款", "="*12)
        deposit(account)
        input("按回车继续： ")
    elif key == '3':
        print("=" * 12, "取款", "="*12)
        withdraw(account)
        input("按回车继续： ")
    elif key == '4':
        logOut()
        print("=" * 12, "再见", "="*12)
        break
    else:
        print("=" * 12, "操作无效", "="*12)

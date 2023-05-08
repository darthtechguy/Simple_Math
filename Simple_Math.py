# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27

@author: curtis
"""

import os

def clear_screen():
    os.system('cls')
    
def close():
    print('Exiting the program.')
    exit()

def secret_msg():
    print('\nHey! You found my Easter Egg.\nThis application was created by me Curtis Barry.')

print('Welcome to my simple 2 digit math application.')
print('You must enter 2 digits and choose an operation to apply to the digits.')

def get_input():
    var1 = ''
    while True:
        var1 = input('\nInput your first number (or x to quit): ')
        if var1 == 'x':
            close()
        else:
            try:
                var1 = float(var1)
                break
            except ValueError:
                print('\nPlease input a number or x to quit!')
    while True:
        var2 = input('\nInput your second number (or x to quit): ')
        if var2 == 'x':
            close()
        else:
            try:
                var2 = float(var2)
                break
            except ValueError:
                print('\nPlease input a number or x to quit!')
    return var1, var2

def adder(var1, var2):
    sum = var1 + var2
    if sum < 0:
        sum *= -1
    sum = round(sum,2)
    print('\nThe sum of', var1, 'and', var2, 'is', sum)

def taker(var1, var2):
    sum = var1 - var2
    if sum < 0:
        sum *= -1
    sum = round(sum,2)
    print('\nThe difference of', var1, 'and', var2, 'is', sum)

def multi(var1, var2):
    sum = var1 * var2
    if sum < 0:
        sum *= -1
    sum = round(sum,2)
    print('\nThe product of', var1, 'and', var2, 'is', sum)

def split(var1, var2):
    if var2 == 0:
        print("\nSorry I can't divide by 0")
    else:
        result = var1 / var2
        result = round(result,2)
        print('\n',var1, 'divided by', var2, 'is', result)

while True:
    var1, var2 = get_input()

    choice = input('\nWould you like to add, subtract, multiply, or divide? ')

    if choice == 'add' or choice == '+':
        adder(var1, var2)
    elif choice == 'subtract' or choice == '-':
        taker(var1, var2)
    elif choice == 'multiply' or choice == '*':
        multi(var1, var2)
    elif choice == 'divide' or choice == '/':
        split(var1, var2)
    elif choice == 'CLB':
        secret_msg()
    else:
        print('\nInvalid choice\n')
        continue

    choice2 = input('\nWould you like to start "again", or "exit"? ')
    
    if choice2 == 'again'or choice2 == 'a':
        clear_screen()
        continue
    elif choice2 == 'exit'or choice2 == 'x':
        break


# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:59:36 2022

@author: 2023086
"""

for num in range(1, 101):
    string = ''
    # ここから記述
    
    if num % 15 == 0:
        string = "FizzBuzz"
    elif num % 3 == 0:
        string = "Fizz"
    elif num % 5 == 0:
        string = 'Buzz'
    else:
        string = num
    # ここまで記述
    print(string)
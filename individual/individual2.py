# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Составить программу нахождения из трех чисел наибольшего и наименьшего.
"""

if __name__ == '__main__':
    print("Введите три числа")
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    c = int(input("Третье число: "))

    if b > a < c:
        print("Наименьшее: ", a)
    elif a > b < c:
        print("Наименьшее: ", b)
    else:
        print("Наименьшее: ", c)

    if b < a > c:
        print("Наибольшее: ", a)
    elif a < b > c:
        print("Наибольшее: ", b)
    else:
        print("Наибольшее: ", c)

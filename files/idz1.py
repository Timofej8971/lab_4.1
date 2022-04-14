#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Поле first — дробное число, левая граница диапазона; поле second — дробное число,
правая граница диапазона. Реализовать метод rangecheck() — проверку заданного числа
на принадлежность диапазону.
'''


def make_class(first, second, third):
    if first > second:
        raise ValueError()
    else:
        return MyClass(first, second, third)


class MyClass:

    def __init__(self, first=0, second=0, third=0):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)
        self.otvet = ""

    def read(self):
        self.first = float(input("Введите начало диапазона: "))
        self.second = float(input("Введите конец диапазона: "))
        self.third = float(input("Введите число для проверки принадлежности к диапазону: "))

    def display(self):
        print(f"Указанное число: {self.otvet}")

    def rangecheck(self):
        if self.first < self.second and self.first < self.third < self.second:
            self.otvet = "внутри диапозона"
        else:
            self.otvet = "за пределами диапозона"


if __name__ == '__main__':
    work = make_class(1, 5, 7)
    work.rangecheck()
    work.display()
    

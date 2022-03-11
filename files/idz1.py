#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Поле first — дробное число, левая граница диапазона; поле second — дробное число,
правая граница диапазона. Реализовать метод rangecheck() — проверку заданного числа
на принадлежность диапазону.
'''


class MyClass:

    def __init__(self, first=0, second=0, third=0):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    def read(self):
        first = input("Введите начало диапазона: ")
        second = input("Введите конец диапазона: ")
        third = input("Введите число для проверки принадлежности к диапазону: ")

        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    def display(self):
        print(f"Указанное число: {rangecheck(self)}")


def rangecheck(self):
    if self.first < self.second and self.first < self.third <self.second:
        return "внутри диапозона"
    elif self.first >= self.second:
        raise ValueError("Неверный диапозон")
    else:
        return "за пределами диапозона"


if __name__ == '__main__':
    work = MyClass()
    work.read()
    work.display()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
(например, «2004.08.31») и датой. Обязательными операциями являются: вычисление даты
через заданное количество дней, вычитание заданного количества дней из даты,
определение високосности года, присвоение и получение отдельных частей (год, месяц,
день), сравнение дат (равно, до, после), вычисление количества дней между датами.
"""


import datetime


class Date:

    def __init__(self, year=None, month=None, day=None, str_date=None, number_of_days=1):
        # date = datetime.date(year, month, day)
        # str_date = datetime.datetime.strptime(str_date, "%Y-%m-%d")
        self.number_of_days = int(number_of_days)
        self.today_day = datetime.date.today()

        if year == None and str_date != None:
            self.first_date = datetime.datetime.strptime(str_date, "%Y-%m-%d").day
        elif year != None and str_date == None:
            self.first_date = datetime.date(year, month, day)

        # self.second_date = datetime.datetime.strptime(second_date, "%Y-%m-%d")
        self.second_date = None
        self.date_from_nub = None
        self.date_minus_day = None
        self.leap_year_date = None
        self.comparison_result = None
        self.between_dates_numb = None

    def read(self):
        number_of_days = int(input("Введите количество дней для операций:"))
        self.number_of_days = number_of_days
        second_date = input("Введите дату для сравнения в фомате Y-m-d: ")
        self.second_date = datetime.datetime.strptime(second_date, "%Y-%m-%d").day

    def display(self):
        display_text = f'''
Дата указанная при обьявлении класса: {self.first_date}
Дата внесённая пользователем: {self.second_date}
Количество дней используемых для выполнения вычислений: {self.number_of_days}
Дата через заданное количесвто дней: {self.date_from_nub}
Дата минус заданное количесвто дней: {self.date_minus_day()}
Указанный год: {self.leap_year_date}
Первая дата {self.comparison_result} второй
Между датами прошло: {self.between_dates_numb} 
'''
        print(display_text)

    def date_from_number(self):
        self.date_from_nub = self.today_day + datetime.timedelta(days=self.number_of_days)

    def date_minus_days(self):
        self.date_minus_day = self.first_date - datetime.timedelta(days=self.number_of_days)

    def leap_year(self):
        year = self.first_date.year
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            self.leap_year_date = "високосный"
        else:
            self.leap_year_date = "не високосный"

    def comparison(self):
        if self.first_date > self.second_date:
            self.comparison_result = "больше"
        elif self.first_date == self.second_date:
            self.comparison_result = "равна"
        else:
            self.comparison_result = "меньше"

    def between_dates(self):
        if self.comparison_result == "меньше":
            self.between_dates_numb = (self.second_date - self.first_date).days
        else:
            self.between_dates_numb = (self.first_date - self.second_date).days


if __name__ == '__main__':
    work = Date(str_date="2022-12-11")
    work.read()
    work.date_from_number()
    work.date_minus_days()
    work.leap_year()
    work.comparison()
    work.between_dates()
    work.display()
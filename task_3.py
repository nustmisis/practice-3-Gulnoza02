# -*- coding: utf-8 -*-
"""
Если вы когда-нибудь пытались собирать номера мобильных телефонов, то наверняка
знаете, что почти любые 10 человек используют как минимум пяток различных
способов записать номер телефона. Кто-то начинает с +7, кто-то просто с 7 или 8,
а некоторые вообще не пишут префикс. Трёхзначный код кто-то отделяет пробелами,
кто-то при помощи дефиса, кто-то скобками (и после скобки ещё пробел некоторые
добавляют). После следующих трёх цифр кто-то ставит пробел, кто-то дефис, кто-то
ничего не ставит. И после следующих двух цифр — тоже. А некоторые начинают за
здравие, а заканчивают… В общем очень неудобно!

На вход даётся номер телефона в России, как его мог бы ввести человек.
Необходимо его переформатировать в формат +7 123 456-78-90. Если с номером
что-то не так, то нужно вывести строчку Fail!

Примеры:

# | Ввод                Вывод
--+-------------------------------------
1 | +7 123 456-78-90    +7 123 456-78-90
2 | 8(123)456-78-90     +7 123 456-78-90
3 | 1234567890          +7 123 456-78-90
4 | 123456789           Fail!
5 | +9 123 456-78-90    Fail!
6 | +7 123 456+78=90    Fail!

Для корректной работы автоматических тестов не переименовывайте функцию
format_phone_number!
"""

import re
def format_phone_number(text):
    # ваше решение:
 print(format_phone_number("+7 123 456-78-90"))  # Вывод: +7 123 456-78-90
print(format_phone_number("8(123)456-78-90"))  # Вывод: +7 123 456-78-90
print(format_phone_number("1234567890"))       # Вывод: +7 123 456-78-90
print(format_phone_number("123456789"))        # Вывод: Fail!
print(format_phone_number("+9 123 456-78-90"))  # Вывод: Fail!
print(format_phone_number("+7 123 456+78=90"))  # Вывод: Fail!
"return"  "Fail!"

# Консольное приложение для работы с погодой
# Консольное меню:
# 1 - ввод температуры за неделю
# 2 - вывод температуры за неделю на экран
# 3 - запись температуры в файл
# 4 - чтение температуры из файла
# 5 - вывод максимальной и минимальной температуры
# 6 - и тд
# Q - выход, т.е. конец работы программы

# file_functions - функции для работы с файлами, а именно чтение и запись
# UI - User Interface menu() - просто выводит список меню
# statistic - обработка информации о погоде(мин/макс, предсказание и тд)
# main - основная программа
from Statistic import *
from UI import *

user_choise = ""
while user_choise != 'Q':
    menu()
    user_choise = input()
    if user_choise == "1":
        temp = temp_input()
    if user_choise == "2":
        sep =input("Выбор разделителя")
        temp_output(temp, sep)
    if user_choise == "3":
        pass
# Консольное приложение для работы с погодой
# Консольное меню:
# 1 - ввод температуры за неделю
# 2 - вывод температуры за неделю на экран
# 3 - запись температуры в файл
# 4 - чтение температуры из файла
# 5 - вывод максимальной и минимальной температуры
# 6 - Функция выводит количество "хороших" дней. Хорошие дни - температура в них лежит в каком то промежутке
# Функция принимает на вход список и два числа(границы диапазона). Возвращает одно число - количество хороших днец
# Q - выход, т.е. конец работы программы

# file_functions - функции для работы с файлами, а именно чтение и запись
# UI - User Interface menu() - просто выводит список меню
# statistic - обработка информации о погоде(мин/макс, предсказание и тд)
# main - основная программа
from Statistic import *
from UI import *
from file_work import *
from intput_out import *
from file_work import *
user_choise = ""
temp = [23, 24, 26, 27, 26, 27, 24]
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
    if user_choise == "5":
        print(get_info(temp))
    if user_choise == "6":
        lower_temp = float(input("Введите нижнюю границу температур"))
        higher_temp = float(input("Введите верхнюю границу ввода"))
        print(good_days(temp, lower_temp, higher_temp))
    if user_choise == "7":
        print(frost(temp))
    if user_choise == "8":
        print(avr_week(temp))
    if user_choise == "9":
        print(temp_hole(temp))
    if user_choise == "3":
        print("Запись данных в файл")
    if user_choise == "4":
        print(read_file(temp))






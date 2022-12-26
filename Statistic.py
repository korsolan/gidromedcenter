def temp_input():
    temp = []

    for i in range(7):
        number = float(input("Введи число"))
        temp.append(number)
    return temp

def temp_output(list_temp, sep):
    for i in range(len(list_temp)):
        print(list_temp[i],sep, end= " ")

def get_info(list_temp):
    min_temp = min(list_temp)
    max_temp = max(list_temp)
    return min_temp, max_temp
def good_days(list_temp, lower_temp, higher_temp):
    count = 0
    for i in range(len(list_temp)):
        if lower_temp <= list_temp[i] <= higher_temp:
            count += 1
    return count
def frost (list_temp):
    count = 0
    for i in range(len(list_temp)):
        if list_temp[i] < 0:
            count += 0
    return count
def avr_week (list_temp):
    for i in range(len(list_temp)):
        avr = round(sum(list_temp) / len(list_temp), 2)
    return avr
def temp_hole(list_temp):
    count = 0
    for i in range(1, len(list_temp) - 1):
        if list_temp[i - 1] > list_temp[i] < list_temp[i + 1]:
            count += 1
    return count






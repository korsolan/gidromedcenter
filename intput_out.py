def temp_input():
    temp = []
    for i in range(7):
        number = float(input("Введи число"))
        temp.append(number)
    return temp
def temp_output(list_temp, sep):
    for i in range(len(list_temp)):
        print(list_temp[i],sep, end= " ")
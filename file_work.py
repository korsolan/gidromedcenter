def write_file(filename, datalist):
    f = open(filename + "txt", "w")
    for i in range(len(datalist)):
        f.write(str(datalist[i]) + " ")
    f.close()
def read_file(filename):
    f = open(filename + "txt", "r")
    d = f.readline()
    f.close()
    return d

# def read_file(name):
#     try:
#         file = open("temp.txt", "r")
#     except FileNotFoundError:
#         print("Файл не найден")
#     else:
#         pass
#     return file

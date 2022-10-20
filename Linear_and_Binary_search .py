# Линейный поиск
# Бинарный поиск

# ls = [1, 6, 4, 3, 4, 5, 6, 7, 8, 9, 4, 3]
# value = 4

# 1) True
# 2.1)вхождение first --> index = 2
# 2.2)вхождение last --> index = -2
# 3) count --> 3

# value = 41
# 1) False
# 2.1)вхождение first --> index = -1 (если не найден результат)
# 2.2)вхождение last --> index = -1 (если не найден результат)
# 3) count --> 0
###############################################################################################################
# TRUE / FALSE
def find_value(ls, value):
    answer = False
    for item in ls:
        if item == value:
            answer = True
            break

    return answer

# Цикл без доп переменной
# def find_value(ls, value):
#     for item in ls:
#         if item == value:
#             return True
#
#     return False

def main():
    ls = []
    print ("Input elements of list: ")

    while True:
        number = input ("element: ")
        if number == 'q':
            break

        ls.append(int(number))

    value = int(input("input value: "))

    result = find_value(ls, value)

    msg = "Yes" if result else "No"
    print(ls)
    print(msg)


main()


##################################################################################
# in и not in
# ls = [1, 2, 3, 4, 5, 6]
# value = 4
# print(value in ls)


#################################
# ПЕРВОЕ И ПОСЛЕДНЕЕ ВХОЖДЕНИЕ
# def find_first_index_value(ls,value):
#     for index in range(len(ls)):
#         if ls[index] == value:
#             return index
#     return -1
#
#
# def find_last_index_value(ls, value):
#     for index in range(len(ls)-1, -1, -1):
#         if ls[index] == value:
#             return index
#     return -1

#########################################################################################
# count СОСЧИТАТЬ КОЛИЧЕСТВО VALUE В LS
def count_value(ls, value):
    count = 0

    for item in ls:
        if item == value:
            count+=1
    return count

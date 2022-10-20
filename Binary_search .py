# БИНАРНЫЙ АЛГОРИТМ ПОИСКА BINARY SEARCH
# middle = (left+right)//2  середина промежутка
#
# value == mid --> return True
# value > mid --> left = mid + 1
# value < mid --> right = mid - 1
# while left <= right or right <= left

def binary_search(ls, value):
    count = 0
    left = 0
    right = len(ls) - 1

    while left <= right:
        count += 1  #debug
        middle = (left + right) // 2
        if ls[middle] == value:
            print("Count = " + str(count))  #debug
            return True
        elif ls[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    print("Count = " + str(count))  #debug
    return False


def main():
    ls = [221, 34, 45, 56, 75, 86, 91]
    #Генератор
    ls = [i for i in range(1_000_000_000)]

    print("Linear search: ")
    print(Task02.find_value(ls, 1_000_000_000)) #debug

    print("Binary search: ")
    print(binary_search(ls, 1_000_000_000))


main()

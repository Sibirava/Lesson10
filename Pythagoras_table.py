#Таблица Пифагора (таблица умножения)
def get_pythagoras_table(number):
    table = ""

    for j in range(1, number + 1):
        for i in range(1, number + 1):
            # table += str(i) + ' '
            table += f"{i * j}\t"

        table += "\n"

    return (table)


def main():
    number = int(input("Input size of a table: "))
    table = get_pythagoras_table(number)
    print(table)


main()

# for i in range(1, 10):
#     for k in range(2, 10):
#         print(f'{i} * {k} = {i * k}\t', end='')
#     print('')
# else:
#     print("It's off")

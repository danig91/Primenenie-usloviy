# Напишите программу, которая вычисляет сумму всех четных чисел от 1 до 100.
#
# Создайте список, содержащий квадраты всех нечетных чисел от 1 до 10,
# используя генератор списка.
#
# Напишите программу, которая просит пользователя ввести число
# и продолжает запрашивать числа, пока пользователь не введет отрицательное число.
# Затем программа должна вывести количество введенных чисел.

def calculates_sum_even_numbers(one_hundred):
    sum_number = 0
    for num_1 in range(1, one_hundred + 1):
        if num_1 % 2 == 0:
            sum_number += num_1
    return sum_number


def list_squares_not_even_numbers(ten):
    list_not_even_numbers = []
    for num2 in range(1, ten):
        if num2 % 2 != 0:
            list_not_even_numbers.append(num2)
    squares = [n ** 2 for n in list_not_even_numbers]
    return squares


print(f"Сумма всех чётных чисел от 1 до 100 включительно - "
      f"{calculates_sum_even_numbers(100)}")
print(f"Список, содержащий квадраты всех нечётных чисел от 1 до 10 - "
      f"{list_squares_not_even_numbers(10)}")

list_positive_number = []
entered_numbers = 0
while True:
    try:
        positive_number = float(input("Введите положительное число: "))
        if positive_number > 0:
            list_positive_number.append(positive_number)
        elif positive_number == 0:
            print("\"0\" не является положительным числом!")
        else:
            for _ in list_positive_number:
                entered_numbers += 1
            print(f"Ввод отрицательного значения!\nПоложительных чисел введено:"
                  f" {entered_numbers}\nЗавершение программы.")
            break
    except ValueError:
        print("Ввод нечислового значения!")

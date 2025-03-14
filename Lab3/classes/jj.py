def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Ввод списка
numbers = list(map(int, input("Введите числа через пробел: ").split()))

# Вызов функции
even_numbers = get_even_numbers(numbers)

# Вывод результата
print(even_numbers)
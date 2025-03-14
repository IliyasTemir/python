def all_elements_true(t):
    """Проверяет, все ли элементы в кортеже истинные."""
    return all(t)  # Встроенная функция all() проверяет истинность всех элементов

if __name__ == "__main__":
    user_input = input("Введите элементы кортежа через запятую: ")  
    user_tuple = tuple(map(str.strip, user_input.split(",")))  # Создаем кортеж из ввода, удаляя пробелы
    
    # Преобразуем строки в их истинные значения (пустая строка = False, числа 0 = False и т.д.)
    processed_tuple = tuple(bool(eval(x)) if x.isdigit() or x in ["0", "1"] else bool(x) for x in user_tuple)

    print(f"Кортеж: {processed_tuple}")
    print("✅ Все элементы истинные!" if all_elements_true(processed_tuple) else "❌ Не все элементы истинные.")

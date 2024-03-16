def binary_search(data, target):
    """
        Функция для выполнения бинарного поиска в данных.

        Args:
            data (list): Список строк для поиска.
            target (str): Целевая фамилия пользователя.

        Returns:
            str: Предсказание, если найдено, иначе None.
        """
    for line in data:
        parts = line.split('=')
        user = parts[1].split()[0]  # Берем только фамилию пользователя

        if user == target:
            return parts[2]

    return None

# Открываем файл для чтения
with open('history_mirror.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Запуск консольной программы
while True:
    user_input = input("Введите фамилию пользователя (для выхода введите 'mirror'): ")

    if user_input == 'mirror':
        break

    prediction = binary_search(lines, user_input)

    if prediction:
        print(f"Предсказание для {user_input} - {prediction}")
    else:
        print("Вы не использовали зеркало")
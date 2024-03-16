def check_mirror_balance(data):
    """
        Функция для проверки баланса запросов в данных.

        Args:
            data (list): Список строк для анализа.

        Returns:
            str: Результат проверки баланса запросов.
        """
    stack = []

    for line in data:
        parts = line.split('=')
        verdict = parts[2].strip()

        if verdict == 'Изменение характера':
            stack.append(verdict)
        elif verdict == 'Признание своей уникальности':
            if not stack or stack[-1] != 'Изменение характера':
                return "Запросы не изолированные"
            stack.pop()

    if not stack:
        return "Запросы изолированные"
    else:
        return "Запросы не изолированные"

# Открываем файл для чтения
with open('history_mirror.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

result = check_mirror_balance(lines)
print(result)
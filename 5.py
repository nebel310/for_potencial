def count_verdicts(data):
    """
        Функция для подсчета количества каждого вердикта в данных.

        Args:
            data (list): Список строк для анализа.

        Returns:
            dict: Словарь с количеством каждого вердикта.
        """
    verdict_counts = {}

    for line in data:
        parts = line.split('=')
        verdict = parts[2].strip()

        if verdict in verdict_counts:
            verdict_counts[verdict] += 1
        else:
            verdict_counts[verdict] = 1

    return verdict_counts

# Открываем файл для чтения
with open('history_mirror.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

verdict_counts = count_verdicts(lines)

# Сортируем запросы по количеству и выводим 5 самых популярных
sorted_verdicts = sorted(verdict_counts.items(), key=lambda x: x[1], reverse=True)

for i in range(5):
    print(f"{sorted_verdicts[i][0]} - {sorted_verdicts[i][1]}")
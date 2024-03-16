# Открываем файл для чтения
with open('history_mirror.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Сортировка вставками
for i in range(1, len(lines)):
    key = lines[i]
    j = i - 1
    while j >= 0 and key < lines[j]:
        lines[j + 1] = lines[j]
        j -= 1
    lines[j + 1] = key

# Выводим первые пять самых ранних использований
for line in lines[:5]:
    print(line.strip())
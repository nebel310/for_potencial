# Открываем файл для чтения
with open('history_mirror.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Создаем файл для записи ошибок
with open('mirror_error.txt', 'w', encoding='utf-8') as error_file:
    latest_error_date = None
    latest_error_user = None

    # Проходим по каждой строке
    for line in lines[1:]:  # Пропускаем заголовок
        parts = line.strip().split('=')
        date = parts[0]
        user = parts[1]
        verdict = parts[2]

        # Проверяем наличие ошибки
        if verdict == 'error':
            # Записываем информацию об ошибке в файл
            error_file.write(f'У пользователя {user} {date} появилась ошибка\n')

            # Обновляем самую позднюю ошибку
            if latest_error_date is None or date > latest_error_date:
                latest_error_date = date
                latest_error_user = user

    # Выводим информацию о самой поздней ошибке в консоль
    print(f'Ошибка была зафиксирована: {latest_error_date} у пользователя {latest_error_user}')
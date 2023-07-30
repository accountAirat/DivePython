def school_print(**kwargs):  # **kwargs создаёт словарь
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')  # Принт внутри функции не использовать


school_print(химия=5, физика=4, математика=5, физра=5)

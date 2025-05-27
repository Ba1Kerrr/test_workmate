import argparse
import sys

# Функция для парсинга аргументов командной строки
def parse_args():
    """
    Парсит аргументы командной строки.
    
    Возвращает:
    argparse.Namespace: Объект с аргументами командной строки.
    """
    parser = argparse.ArgumentParser(description='Скрипт подсчёта зарплаты сотрудников')
    # Добавляем аргумент для указания файлов с данными сотрудников
    parser.add_argument('files', nargs='+', help='Пути к файлам с данными сотрудников')
    # Добавляем аргумент для указания типа отчета
    parser.add_argument('--report', choices=['payout'], default='payout', help='Тип отчета')
    return parser.parse_args()

# Функция для чтения данных из файла csv
def read_csv_file(file_path):
    """
    Читает данные из файла csv.
    
    Аргументы:
    file_path (str): Путь к файлу csv.
    
    Возвращает:
    list: Список словарей с данными сотрудников.
    """
    with open(file_path, 'r') as file:
        # Читаем все строки из файла
        lines = file.readlines()
        # Разделяем первую строку на заголовки
        headers = lines[0].strip().split(',')
        # Создаем список для хранения данных сотрудников
        data = []
        # Обрабатываем каждую строку файла
        for line in lines[1:]:
            # Создаем словарь для хранения данных сотрудника
            row = {}
            # Разделяем строку на значения
            values = line.strip().split(',')
            # Обрабатываем каждое значение
            for header, value in zip(headers, values):
                # Добавляем значение в словарь
                row[header] = value
            # Добавляем словарь в список
            data.append(row)
        return data

# Функция для расчета общей зарплатыles
def calculate_payout(data):
    """
    Рассчитывает общую зарплату.
    
    Аргументы:
    data (list): Список словарей с данными сотрудников.
    
    Возвращает:
    int: Общая зарплата.
    """
    payout = 0
    # Обрабатываем каждое словарь в списке
    for row in data:
        # Ищем значение заработной платы в час
        hourly_rate = row.get('hourly_rate') or row.get('rate') or row.get('salary')
        # Ищем значение количества отработанных часов
        hours_worked = int(row['hours_worked'])
        # Добавляем зарплату сотрудника к общей зарплате
        payout += int(hourly_rate) * hours_worked
    return payout

# Функция для создания отчета
def generate_report(data, report_type):
    if report_type == 'payout':
        # Рассчитываем общую зарплату
        payout = calculate_payout(data)
        # Группируем участников по сфере деятельности
        departments = {}
        print(f"{' ' * 14}{'name':<20}{'hours':<15}{'rate':<10}{'payout':<10}")
        for row in data:
            department = row['department']
            if department not in departments:
                departments[department] = []
            departments[department].append(row)
        # Выводим отчет
        for department, rows in departments.items():
            print(department)
            for row in rows:
                hourly_rate = row.get('hourly_rate') or row.get('rate') or row.get('salary')
                hours_worked = int(row['hours_worked'])
                salary = int(hourly_rate) * hours_worked
                print(f"{'-' * 14}{row['name']:<20}{hours_worked:<15}{hourly_rate:<10}${salary:<10}")
            print()
        print(f"Общая зарплата: ${payout}")
    else:
        # Возвращаем ошибку, если тип отчета неизвестен
        raise ValueError('Неизвестный тип отчета')
# Основная функция
def main():
    """
    Основная функция.
    """
    # Парсим аргументы командной строки
    args = parse_args()
    # Создаем список для хранения данных сотрудников
    data = []
    # Обрабатываем каждый файл
    for file_path in args.files:
        # Читаем данные из файла
        data.extend(read_csv_file(file_path))
    # Генерируем отчет
    report = generate_report(data, args.report)

# Запускаем основную функцию, если скрипт запущен напрямую
if __name__ == '__main__':
    main()

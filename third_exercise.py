import sys
from collections import Counter
from colorama import Fore, Style
from pathlib import Path

def parse_log_line(line: str) -> dict:
    """Форматування строки в словник. Спочатку йде розділення
     через спліт, а потім додавання до словника"""
    parsed_dict = dict()
    parsed_line = line.strip().split()
    parsed_dict['date'] = parsed_line[0]
    parsed_dict['time'] = parsed_line[1]
    parsed_dict['log_level'] = parsed_line[2]
    parsed_dict['log_message'] = (' ').join(parsed_line[3:])
    return parsed_dict

def load_logs(file_path: str) -> list:
    """Відкриття файлу, зчитування всіх строк через рідлайнз і через мап,
    використовуючи парсування в словник(функція вище), повертається
    список словників з кожного рядка"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(map(parse_log_line, file.readlines()))

def filter_logs_by_level(logs: list, level: str) -> list:
    """В першому рядку фільтруються всі значення за допомогою функцій фільтр і лямбда"""
    log_level_list = list(filter(lambda log: log['log_level'] == level.upper(), logs))
    """В другому рядку через мап і лямбду повертається відформатований рядок із словника"""
    return list(map(lambda log: f"{log['date']} {log['time']} - {log['log_message']}", log_level_list))

def count_logs_by_level(logs: list) -> dict:
    """Підрахування всіх рівнів логу за допомогою Каунтеру"""
    return Counter(map(lambda log: log['log_level'], logs))

def display_log_counts(counts: dict, log_mark=None):
    """Якщо введений рівень логу не співпадає з жодним дійсним, викликається помилка,
    яка обробляєтся в __меін__"""
    if log_mark not in counts and log_mark is not None:
        raise SyntaxWarning
    print('{:<15}|{:<10}'.format('Log level', 'Count'))
    print('-' * 15, '|', '-' * 10, sep='')
    for log_level, count in counts.items():
        """Якщо вказаний рівень логування, який треба вивести окремо, то в 
        основній таблиці він буде зеленого кольору"""
        if log_mark and log_mark.upper() == log_level:
            print(Fore.GREEN + '{:<15}'.format(log_level.upper()) + Style.RESET_ALL + '|{:<10}'.format(count))
        else:
            print('{:<15}|{:<10}'.format(log_level, count))
    if log_mark:
        print('\n')

if __name__ == '__main__':
    try:
        command_line_args = sys.argv
        """Зчитування файлу і перетворення рядків в словник логів"""
        parsed_list_from_file = load_logs(str(Path(command_line_args[1])))
        """Створення словника з підрахунками за рівнем ключа"""
        counter_dict = count_logs_by_level(parsed_list_from_file)
        """Якщо введено біьлша або менша кількість параметрів в командну строку,
        основний скрипт не відпрацює"""
        if len(command_line_args) == 2:
            display_log_counts(counter_dict)
        elif len(command_line_args) == 3:
            display_log_counts(counter_dict, command_line_args[2])
            print(*filter_logs_by_level(parsed_list_from_file, command_line_args[2]), sep='\n')
        else:
            print('Waiting for two or three params. Not more and not less')
    # Обробка помилок
    except FileNotFoundError:  # Невірно вказаний шлях файлу
        print('No such file or directory')
    except PermissionError:    # Вказаний невірний файл або папка
        print('Wrong name of file or permission denied')
    except SyntaxWarning:      # Невірно вказані параметри
        print('No such log level')


"""
Команди для запуску скрипта з командної строки. Приклад:
py third_exercise.py logfile.log   або   py third_exercise.py logfile.log debug


py third_exercise.py logfile.log 
info
debug
error
warning
"""
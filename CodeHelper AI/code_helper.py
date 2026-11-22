
# CodeHelper AI
# A simple assistant for programmers

def explain_code():
    code = input("Введите код Python: ")

    prompt = f"""
Ты помощник программиста.
Объясни данный код простыми словами.
Расскажи, что делает каждая важная часть программы.
В конце приведи краткий итог.

Код:
{code}
"""
    print("\nПромпт для ChatGPT:")
    print(prompt)


def find_error():
    code = input("Введите код с ошибкой: ")

    prompt = f"""
Ты специалист по Python.
Проанализируй данный код.
Найди возможные ошибки.
Объясни причину ошибки и предложи исправленный вариант.

Код:
{code}
"""
    print("\nПромпт для ChatGPT:")
    print(prompt)


def create_tests():
    code = input("Введите функцию Python: ")

    prompt = f"""
Ты опытный Python-разработчик.
Создай тесты для данной функции.
Проверь обычные значения, граничные случаи
и неправильные входные данные.
Используй модуль unittest.
Выведи готовый код тестов.

Функция:
{code}
"""
    print("\nПромпт для ChatGPT:")
    print(prompt)


def create_documentation():
    code = input("Введите код функции: ")

    prompt = f"""
Напиши документацию к данному коду Python.
Укажи:
1. Назначение функции.
2. Параметры.
3. Что возвращает функция.
4. Пример использования.

Используй простой и понятный язык.

Код:
{code}
"""
    print("\nПромпт для ChatGPT:")
    print(prompt)


def check_code():
    code = input("Введите код для проверки: ")

    prompt = f"""
Ты проводишь проверку Python-кода.
Найди возможные проблемы:
1. Ошибки в логике.
2. Повторение кода.
3. Неудачные названия переменных.
4. Возможные проблемы с производительностью.

Для каждой проблемы предложи решение.
Не изменяй код без объяснения.

Код:
{code}
"""
    print("\nПромпт для ChatGPT:")
    print(prompt)


def main():
    while True:
        print("\n===== CodeHelper AI =====")
        print("1. Объяснение кода")
        print("2. Анализ ошибок")
        print("3. Создание тестов")
        print("4. Создание документации")
        print("5. Поиск проблем в коде")
        print("0. Выход")

        choice = input("Выберите функцию: ")

        if choice == "1":
            explain_code()
        elif choice == "2":
            find_error()
        elif choice == "3":
            create_tests()
        elif choice == "4":
            create_documentation()
        elif choice == "5":
            check_code()
        elif choice == "0":
            print("Работа программы завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


main()

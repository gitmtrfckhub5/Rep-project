
from library import Library


# Создаём библиотеку
library = Library()


# Главное меню
while True:
    print("\n========== БИБЛИОТЕКА ==========")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Найти книгу по автору")
    print("5. Изменить статус книги")
    print("6. Удалить книгу")
    print("7. Редактировать книгу")
    print("8. Создать резервную копию")
    print("9. Восстановить резервную копию")
    print("0. Выход")
    print("================================")

    choice = input("Выберите действие: ")

    # Добавление книги
    if choice == "1":
        title = input("Введите название книги: ")
        author = input("Введите автора: ")

        try:
            year = int(input("Введите год издания: "))

            if title.strip() == "" or author.strip() == "":
                print("Название и автор не должны быть пустыми.")
            elif year <= 0:
                print("Год должен быть положительным числом.")
            else:
                library.add_book(title, author, year)

        except ValueError:
            print("Год должен быть числом.")

    # Просмотр всех книг
    elif choice == "2":
        library.show_books()

    # Поиск по названию
    elif choice == "3":
        title = input("Введите название книги: ")
        library.search_by_title(title)

    # Поиск по автору
    elif choice == "4":
        author = input("Введите автора: ")
        library.search_by_author(author)

    # Изменение статуса
    elif choice == "5":
        try:
            book_id = int(input("Введите ID книги: "))
            library.change_status(book_id)
        except ValueError:
            print("ID должен быть числом.")

    # Удаление книги
    elif choice == "6":
        try:
            book_id = int(input("Введите ID книги: "))
            library.delete_book(book_id)
        except ValueError:
            print("ID должен быть числом.")

    # Редактирование книги
    elif choice == "7":
        try:
            book_id = int(input("Введите ID книги: "))
            library.edit_book(book_id)
        except ValueError:
            print("ID должен быть числом.")

    # Создание резервной копии
    elif choice == "8":
        library.create_backup()

    # Восстановление резервной копии
    elif choice == "9":
        library.restore_backup()

    # Выход
    elif choice == "0":
        library.save_books()
        print("Данные сохранены. До свидания!")
        break

    else:
        print("Неверный пункт меню.")

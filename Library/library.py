
import json
import pickle
from book import Book


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    # Загрузка книг из файла
    def load_books(self):
        try:
            with open("books.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                for item in data:
                    book = Book.from_dict(item)
                    self.books.append(book)

            print("Каталог успешно загружен.")

        except FileNotFoundError:
            print("Файл не найден. Будет создан новый каталог.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Ошибка чтения файла. Каталог будет пустым.")
            self.books = []

    # Сохранение книг
    def save_books(self):
        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # Добавление книги
    def add_book(self, title, author, year):
        if len(self.books) == 0:
            new_id = 1
        else:
            new_id = max(book.id for book in self.books) + 1

        book = Book(new_id, title, author, year)

        self.books.append(book)
        self.save_books()

        print("Книга успешно добавлена!")


    # Просмотр всех книг
    def show_books(self):
        if len(self.books) == 0:
            print("Каталог пуст.")
        else:
            print("\n--- Каталог библиотеки ---")

            for book in self.books:
                print(book)


    # Поиск по названию
    def search_by_title(self, title):
        found = False

        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                found = True

        if not found:
            print("Книга не найдена.")

    # Поиск по автору
    def search_by_author(self, author):
        found = False

        for book in self.books:
            if author.lower() in book.author.lower():
                print(book)
                found = True

        if not found:
            print("Книги этого автора не найдены.")

    # Изменение статуса
    def change_status(self, book_id):
        for book in self.books:
            if book.id == book_id:
                book.is_available = not book.is_available
                self.save_books()

                print("Статус книги изменён.")
                return

        print("Книга с таким ID не найдена.")

    # Удаление книги
    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()

                print("Книга удалена.")
                return

        print("Книга с таким ID не найдена.")

    # Редактирование книги
    def edit_book(self, book_id):
        for book in self.books:
            if book.id == book_id:

                print("Введите новые данные.")
                print("Чтобы оставить старое значение, нажмите Enter.")

                title = input("Новое название: ")
                author = input("Новый автор: ")
                year = input("Новый год: ")

                if title != "":
                    book.title = title

                if author != "":
                    book.author = author

                if year != "":
                    try:
                        book.year = int(year)
                    except ValueError:
                        print("Год должен быть числом.")

                self.save_books()
                print("Информация изменена.")
                return

        print("Книга с таким ID не найдена.")

    # Создание резервной копии
    def create_backup(self):
        try:
            with open("books_backup.pkl", "wb") as file:
                pickle.dump(self.books, file)

            print("Резервная копия создана.")

        except Exception as error:
            print("Ошибка:", error)

    # Восстановление резервной копии
    def restore_backup(self):
        try:
            with open("books_backup.pkl", "rb") as file:
                self.books = pickle.load(file)

            self.save_books()
            print("Каталог восстановлен.")

        except FileNotFoundError:
            print("Резервная копия не найдена.")

        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError):
            print("Ошибка чтения резервной копии.")

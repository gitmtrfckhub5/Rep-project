
class Book:
    def __init__(self, id, title, author, year, is_available=True):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    # Преобразование книги в словарь
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available
        }

    # Создание книги из словаря
    @staticmethod
    def from_dict(data):
        return Book(
            data["id"],
            data["title"],
            data["author"],
            data["year"],
            data["is_available"]
        )

    # Вывод информации о книге
    def __str__(self):
        if self.is_available:
            status = "Доступна"
        else:
            status = "Выдана"

        return (f"ID: {self.id} | "
                f"Название: {self.title} | "
                f"Автор: {self.author} | "
                f"Год: {self.year} | "
                f"Статус: {status}")

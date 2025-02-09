class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name  # Атрибут _name
        self._author = author  # Атрибут _author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Проверка на pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Проверка на duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Продолжительность книги должна быть числом с плавающей запятой.")
        if value <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration} ч."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


#Проверка работы Классов

# Тест для  Book
book1 = Book("Гарри Поттер", "Джоан Роулинг")
print(book1)  # Книга Гарри Поттер. Автор Джоан Роулинг
print(repr(book1))  # Book(name='Гарри Поттер', author='Джоан Роулинг')

# Тест для PaperBook
paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
print(paper_book)
print(repr(paper_book))  # PaperBook(name='1984', author='Джордж Оруэлл', pages=328)

# Тест для AudioBook
audio_book = AudioBook("Вино из одуванчиков", "Рэй Дуглас Брэдбери", 5.5)
print(audio_book)
print(repr(audio_book))  # AudioBook(name='Слушай', author='Автор Аудиокниги', duration=5.5)

# Проверка на ошибки
try:
    invalid_paper_book = PaperBook("МЫ", "Евгений Замятин", -5)
except ValueError as e:
    print(f"Ошибка при создании бумажной книги: {e}")

try:
    invalid_audio_book = AudioBook("Вино из одуванчиков", "Рэй Дуглас Брэдбери", -2.5)
except ValueError as e:
    print(f"Ошибка при создании аудиокниги: {e}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}'


class Bookcase:
    def __init__(self, books):
        self.books = self.create_books(books)
        pass

    def create_books(self, books):
        return [Book(t, a) for t, a in books]
        # return [Book(b.title, b.author) for b in books]

    def __iter__(self):
        for book in self.books:
            yield str(book) # generator


book1 = Book("The old man", "Ernest Hemingway")
book2 = Book("Beyond Good and Evil", "Friedrich Nietzsche")

print(str(book1))
print(str(book2))

bookcase1 = Bookcase([("The old man", "Ernest Hemingway"), ("Beyond Good and Evil", "Friedrich Nietzsche")])
print(bookcase1)
for book in bookcase1:
    print(book)


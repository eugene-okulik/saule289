class Book:
    def __init__(self, material, text, book_name, author, pages, ISBN, reserve=False):
        self.material = material
        self.text = text
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.isbn = ISBN
        self.reserve = reserve


class Detective(Book):
    def __init__(self, material, text, book_name, author, pages, ISBN, reserve, main_character):
        super().__init__(material, text, book_name, author, pages, ISBN, reserve)
        self.main_character = main_character


class Classic(Book):
    school_literature: True
    type = 'classic'


sherlok_holmes = Detective('paper', 'available', 'The Hound of the Baskervilles',
                           'Arthur Conan Doyle', '100', '9781234567897',
                           True, 'Sherlock Holmes')

poirot = Detective('paper', 'available', 'A Haunting in Venice',
                   'Agatha Christie', '99', '456789712345',
                   False, 'Hercule Poirot')

pushkin = Classic('online', 'available', 'Eugene Onegin', 'Alexander Pushkin',
                  '120', '9781234567897', False)

lermontov = Classic('online', 'available', 'The Cliff', 'Michail Lermintov',
                    '50', '9781234567897', False)

harry_potter = Classic('online', 'available', 'The Harry Potter', 'Joanne Rowling',
                       '300', '9781234567897', False)

books = [sherlok_holmes, poirot, pushkin, lermontov, harry_potter]

for book in books:
    if book.reserve:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages}, "
              f"материал: {book.material}, зарезервирована")
    else:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages}, материал: {book.material}")

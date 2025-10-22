from book_class import Book


class SchoolClass(Book):
    def __init__(self, material, text, book_name, author, pages, ISBN, reserve, subject, school_class, tasks=False):
        super().__init__(material, text, book_name, author, pages, ISBN, reserve)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks


math = SchoolClass('paper', 'available', 'Simple Maths', 'Peterson', '200',
                   '9781234567897', True, 'Mathematics', 11, True)
literature = SchoolClass('paper', 'available', 'The Great Words', 'Mikheev', '300',
                         '9781234567897', False, 'Literature', 7, False)
physics = SchoolClass('paper', 'available', 'Phisics Basics', 'Enstein', '2000',
                      '9781234567897', False, 'Physics', 10, True)

textbooks = [math, literature, physics]
for book in textbooks:
    if book.reserve:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages}, "
              f"предмет: {book.subject}, класс: {book.school_class}, зарезервирована")
    else:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages}, "
              f"предмет: {book.subject}, класс: {book.school_class}")

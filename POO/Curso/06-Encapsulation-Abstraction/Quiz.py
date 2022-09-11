class Book:

	def __init__(self, title, author, num_pages, ISBN, publisher):
		self.title = title
		self._author = author
		self.__num_pages = num_pages
		self._ISBN = ISBN
		self.publisher = publisher
  
my_book = Book('Clean Code', 'Emill', 300 , 'ISBN57896',2005)

print(my_book._Book__num_pages)#300

my_book._Book__num_pages = 800

print(my_book._Book__num_pages)#800

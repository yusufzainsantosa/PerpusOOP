from operator import itemgetter
from modules.json_handling import add_data_to_file, filter_data_by_id, open_file, remove_data_by_id

class Book:
  __path = 'book.json'
  __book_format = ['title', 'author', 'description', 'total_copy']

  def __init__(self):
    self.__id = None
    self.__title = None
    self.__author = None
    self.__description = None
    self.__total_copy = None
    self.__present_copy = None
    self.__list_book = []
    
    self.__reload()

  @property
  def current_book(self):
    return {      
      "title" : self.__title,
      "author" : self.__author,
      "description" : self.__description,
      "total_copy" : self.__total_copy,
      "present_copy" : self.__present_copy,
    }

  @property
  def list_book(self):    
    self.__reload()

    return self.__list_book

  @list_book.setter
  def list_book(self, book):
    try:
      self.__reload()
      self.__validate(**book)
      self.__set_data(**book)
    except ValueError as error:
      raise ValueError(error)
    
    data_book = self.book_by_id
    print('data_book: ', self.__description)
    # _, data = itemgetter("message", "data")(add_data_to_file(self.__path, **data_book))
    # self.__set_data(**data)

  @property
  def book_by_id(self):
    data = self.current_book
    if self.__id is not None:
      data['id'] = self.__id
      return data
    return {}

  @book_by_id.setter
  def book_by_id(self, id):
    data = filter_data_by_id(Book.__path, id)
    if data.get('id') is not None:
      self.__set_data(**data)

  @book_by_id.deleter
  def book_by_id(self):
    if self.__id is not None:
      remove_data_by_id(Book.__path, self.__id)
      return { 'message': 'Data successfully deleted' }
    return { 'message': 'id not found, please set the id' }

  def __validate(self, **book):
    for item in Book.__book_format:
      if (book.get(item) == None):
        raise ValueError('Please enter a {} to add the book to the list'.format(item))

    return { 'message': 'Book is verified' }
  
  def __set_data(self, **book):   
    if (book.get('id')):
      self.__id = book['id'] 
    self.__title = book['title']
    self.__author = book['author']
    self.__description = book['description']
    self.__total_copy = book['total_copy']
    self.__present_copy = book['present_copy']
  
  def __reload(self):    
    self.__list_book = open_file(Book.__path)

    return self.__list_book

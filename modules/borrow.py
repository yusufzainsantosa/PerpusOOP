from modules.book import Book
from modules.user import User
from modules.json_handling import add_data_to_file, filter_data_by_id, open_file, remove_data_by_id

class Borrow(Book, User):
  __path = 'borrow.json'
  __borrow_format = ['borrowed_by', 'book_id']

  def __init__(self):
    self.__borrowed_by = None
    self.__date_borrowed = None
    self.__date_returned = None
    self.__book_id = None
    self.__list_borrow = []
    
    self.__reload()
  
  @property
  def list_borrow(self):
    self.__reload()

    return self.__list_borrow
  
  # def borrow(self, user_id, book_id):
  #   user_data = 
  
  def __reload(self):    
    self.__list_borrow = open_file(Borrow.__path)

    return self.__list_borrow

  
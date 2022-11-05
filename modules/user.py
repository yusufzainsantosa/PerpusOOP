from operator import itemgetter
from modules.json_handling import add_data_to_file, filter_data_by_id, open_file, remove_data_by_id

class User:
  __path = 'user.json'
  __user_format = ['name', 'address', 'birth_date']

  def __init__(self):
    self.__id = None
    self.__name = None
    self.__address = None
    self.__birth_date = None
    self.__is_member = True
    self.__list_user = []
      
    self.__reload()

  @property
  def current_user(self):
    return {      
      "name": self.__name,
      "address": self.__address,
      "birth_date": self.__birth_date,
      "is_member": self.__is_member,
    }

  @property
  def list_user(self):    
    self.__reload()

    return self.__list_user

  @list_user.setter
  def list_user(self, user):
    try:
      self.__reload()
      self.__validate(**user)
      self.__set_data(**user)
    except ValueError as error:
      raise ValueError(error)
    
    data_user = self.user_by_id
    _, data = itemgetter("message", "data")(add_data_to_file(self.__path, **data_user))
    self.__set_data(**data)

  @property
  def user_by_id(self):
    data = self.current_user
    if self.__id is not None:
      data['id'] = self.__id
      return data
    return {}

  @user_by_id.setter
  def user_by_id(self, id):
    data = filter_data_by_id(User.__path, id)
    if data.get('id') is not None:
      self.__set_data(**data)

  @user_by_id.deleter
  def user_by_id(self):
    if self.__id is not None:
      remove_data_by_id(User.__path, self.__id)
      return { 'message': 'Data successfully deleted' }
    return { 'message': 'id not found, please set the id' }

  def __validate(self, **user):
    for item in User.__user_format:
      if (user.get(item) == None):
        raise ValueError('Please enter a {} to add the user to the list'.format(item))

    return { 'message': 'user is verified' }
  
  def __set_data(self, **user):   
    if (user.get('id')):
      self.__id = user['id'] 
    self.__name = user['name']
    self.__address = user['address']
    self.__birth_date = user['birth_date']
    # self.__is_member = user['is_member']
  
  def __reload(self):    
    self.__list_user = open_file(User.__path)

    return self.__list_user

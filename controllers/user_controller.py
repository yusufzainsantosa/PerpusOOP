from __main__ import app
from flask import request

from modules.user import User

@app.get('/user/list')
def get_users():
  user = User()
  return user.list_user, 200

@app.post('/user/add')
def update_users():
  data_request = request.json

  try:
    user = User()
    user.list_user = data_request
  except ValueError as error:
    return { 'error': str(error) }, 500 

  return user.user_by_id, 200  

@app.post('/user/delete')
def delete_users():
  data_request = request.json

  if(data_request.get('id') == None):
    return { "message": "Please input the id" }, 403  

  user = User()
  user.user_by_id = data_request['id']
  del user.user_by_id

  return { "message": "Deleted successfully", "data": user.user_by_id }, 200  

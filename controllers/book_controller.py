from __main__ import app
from flask import request

from modules.book import Book

@app.get('/book/list')
def get_books():
  book = Book()
  return book.list_book, 200

@app.post('/book/add')
def update_books():
  data_request = request.json

  try:
    book = Book()
    book.list_book = data_request
  except ValueError as error:
    return { 'error': str(error) }, 500 

  return book.book_by_id, 200  

@app.post('/book/delete')
def delete_book():
  data_request = request.json

  if(data_request.get('id') == None):
    return { "message": "Please input the id" }, 403  

  book = Book()
  book.book_by_id = data_request['id']
  del book.book_by_id

  return { "message": "Deleted successfully", "data": book.book_by_id }, 200  

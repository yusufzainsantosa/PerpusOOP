import os
import json

data_path = os.path.abspath(
  os.path.join(
    os.path.dirname( __file__ ),
    '..',
    'data'
  )
)

def open_file(file):
  file_path = os.path.abspath(
    os.path.join(data_path, file)
  )

  data = []
  with open(file_path, 'r') as list:
    data = json.load(list)
  
  return data

def save_file(file, data):  
  file_path = os.path.abspath(
    os.path.join(data_path, file)
  )

  json_object = json.dumps(data, indent=4)
  with open(file_path, "w") as file:
      file.write(json_object)

def add_data_to_file(path, **book):
  data = open_file(path)
  data_id = 1
  data_length = len(data)

  if (data_length > 0):
    data_id = data[data_length-1]['id'] + 1

  book['id'] = data_id
  data.append(book)

  save_file(path, data)
  
  return { "message": "Data successfully added", "data": book }

def filter_data_by_id(path, id):
  data = open_file(path)
  data_filter = filter(lambda item: item['id'] == id, data)
  data_to_list = list(data_filter)

  if (len(data_to_list) == 0):
    return {}
  return data_to_list[0]

def remove_data_by_id(path, id):
  data = open_file(path)
  data_filter = filter(lambda item: item['id'] != id, data)
  data_to_list = list(data_filter)

  save_file(path, data_to_list)

  return data_to_list

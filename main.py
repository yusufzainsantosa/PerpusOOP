from flask import Flask

app = Flask(__name__)

import controllers.book_controller
import controllers.user_controller

if (__name__ == '__main__'):
  app.run()
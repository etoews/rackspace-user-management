import os

from flask import Flask

api = Flask(__name__)

@api.route('/')
def index():
    return 'Rackspace User Management'

if __name__ == '__main__':
    api.run(debug=True)

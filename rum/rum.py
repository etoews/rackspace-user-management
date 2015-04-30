import threading

from flask import Flask

from users import users

api = Flask(__name__)
lock = threading.Lock()

user_num = 0

@api.route('/')
def index():
    return 'Rackspace User Management'

@api.route('/user')
def get_user():
    global user_num

    with lock:
        if user_num < len(users):
            bash = "export OS_REGION_NAME=ORD\n"
            bash += "export OS_USERNAME={}\n".format(users[user_num].username)
            bash += "export OS_API_KEY={}\n".format(users[user_num].api_key)
            bash += "export MACHINE_NAME=machine{0:02d}\n".format(user_num)
            user_num += 1
        else:
            bash = "No More Creds\n"

    return bash

@api.route('/reset')
def reset_users():
    global user_num

    with lock:
        user_num = 0

    return "More Creds\n"

if __name__ == '__main__':
    api.run(debug=True)

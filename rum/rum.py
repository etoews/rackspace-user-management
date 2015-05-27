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
            html = "<pre>\n"
            html += "export OS_AUTH_URL=https://identity.api.rackspacecloud.com/v2.0/\n"
            html += "export OS_REGION_NAME=IAD\n"
            html += "export OS_USERNAME={}\n".format(users[user_num].username)
            html += "export OS_PROJECT_NAME={}\n".format(users[user_num].account_num)
            html += "export OS_PASSWORD={}\n".format(users[user_num].password)
            html += "export OS_API_KEY={}\n".format(users[user_num].api_key)
            html += "</pre>\n"
            user_num += 1
        else:
            html = "No More Creds\n"

    return html

@api.route('/reset')
def reset_users():
    global user_num

    with lock:
        user_num = 0

    return "More Creds\n"

if __name__ == '__main__':
    api.run(debug=True)

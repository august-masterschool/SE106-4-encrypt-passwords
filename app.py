from flask import Flask, render_template, request, url_for
from flask_bcrypt import Bcrypt
import json


app = Flask(__name__)
bcrypt = Bcrypt(app)


def register_user(username, password):
    """
    Return True if the user's login credentials were successfully added
    to the users.json file; return False if not.

    :param username: The raw username submitted via the login form
    :param password: The raw password submitted via the login form
    :return: A Boolean value describing whether the credentials were added to users.json
    """

    try:

        new_username_hash = bcrypt.generate_password_hash(username).decode("utf-8")
        new_password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = {
            "username": new_username_hash,
            "password": new_password_hash,
        }

        with open('users.json', 'r') as users_file:
            users_file_contents = users_file.read()
            users = json.loads(users_file_contents)

        users["users"].append(new_user)
        json_object = json.dumps(users, indent=4)

        with open('users.json', 'w') as outfile:
            outfile.write(json_object)

        return True

    except Exception as e:
        print(e)
        return False


def is_valid_user(username, password):
    """
        Return True if the user credentials are valid; False if not.

        :param username: The raw username submitted via the login form
        :param password: The raw password submitted via the login form
        :return: A Boolean value describing whether the credentials are valid
        """

    try:
        with open('users.json', 'r') as users_file:
            users_file_contents = users_file.read()

        json_object = json.loads(users_file_contents)

        if json_object:
            for user in json_object["users"]:
                if bcrypt.check_password_hash(user["username"], username):
                    if bcrypt.check_password_hash(user["password"], password):
                        return True

        else:  # No users yet, so none can be valid
            return False

    except Exception as e:
        print(e)
        return False


@app.route('/', methods=['GET', 'POST'])
def home():
    error = None

    if request.method == 'GET':
        return render_template('index.html', error=error)

    if request.method == 'POST':

        try:
            username = request.form['username']
            password = request.form['password']

            if is_valid_user(username, password):
                return render_template('login_success.html')

            else:
                error = "Invalid credentials"
                return render_template('index.html', error=error)

        except Exception as e:
            print(e)
            return


@app.route('/register', methods=['GET', 'POST'])
def register():

    error = None

    if request.method == 'GET':
        return render_template('register.html', error=error)

    if request.method == 'POST':

        try:
            username = request.form['username']
            password = request.form['password']

            if register_user(username, password):
                return render_template('registration_success.html')
            else:
                error = "Could not register user"
                return render_template('index.html', error=error)

        except Exception as e:
            print(e)
            return


if __name__ == '__main__':
    app.run(debug=True)
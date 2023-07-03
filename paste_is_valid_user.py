"""
Replace the pseudocode in the is_valid_user() function with Python code.
"""

from flask import Flask
from flask_bcrypt import Bcrypt
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)


# This is a helper function, not a Flask route!
def is_valid_user(username, password):
    """
    Return True if the user credentials are valid; return False if not.

    :param username: The raw username submitted via the login form
    :param password: The raw password submitted via the login form
    :return: A Boolean value describing whether the credentials are valid
    """

    try:
        # Open the users.json file and read the contents

        # Convert the contents to a JSON object

        # If the JSON object is not empty, loop through the users
        # and compare the provided username and password to the
        # hashed username and password. Return a Boolean value.

        # If the JSON object is empty, return the opposite Boolean value


    except Exception as e:
        print(e)
        return False


"""
BONUS: Create a Flask route called home() for the root ('/').
    - A GET request to this route should render index.html.
    - A POST request to this route should call the is_valid_user()
      helper function and render the login_success.html file if 
      the login was successful
          - If the login was not successful, do this:
          return render_template('index.html', error="Invalid credentials")
          
Remember to add this code to the bottom of your file so you can test out your code locally:

if __name__ == '__main__':
    app.run(debug=True)
"""
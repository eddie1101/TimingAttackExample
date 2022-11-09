from flask_restful import Resource, request

from hashlib import sha256
from secrets import token_urlsafe

from bad_compare import bad_compare

class UserAPIEndpoint(Resource):

    def __init__(self, *args, **kwargs):
        super(UserAPIEndpoint, self).__init__(*args, **kwargs)
        self.user_data = {}

        hasher = sha256()
        hasher.update("example_password".encode("UTF-8"))
        username = "example_username"
        password = hasher.hexdigest()
        self.user_data[username] = password


    def post(self): #login
        hasher = sha256()
        hasher.update(request.headers.get("password").encode("UTF-8"))
        username = request.headers.get("username")
        password = hasher.hexdigest()

        print(f'Request Received: {username}, {password}')

        if (username in self.user_data and
           bad_compare(self.user_data[username], password)):
            return token_urlsafe()
        else:
            return "Invalid username/password"


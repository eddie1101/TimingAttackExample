from flask_restful import Resource, request

from hashlib import sha256
from secrets import token_urlsafe

from bad_compare import bad_compare

class UserAPIEndpoint(Resource):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.user_data = {}

        hasher = sha256()
        hasher.update("example_password")
        username = "example_username"
        password = hasher.hexdigest()
        self.user_data.put(username, password)


    def post(self): #login
        hasher = sha256()
        hasher.update(request.headers.get("password"))
        username = request.headers.get("username")
        password = hasher.hexdigest()
        
        if (username in self.user_data and
           bad_compare(self.user_data[username], password)):
            return {"sessionKey", token_urlsafe()}
        else:
            return "Invalid username/password"


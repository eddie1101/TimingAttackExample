from flask_restful import Resource, request

from hashlib import sha256
from secrets import token_hex

from bad_compare import bad_compare
from bad_db import db

class UserAPIEndpoint(Resource):

    def __init__(self, *args, **kwargs):
        super(UserAPIEndpoint, self).__init__(*args, **kwargs)


    def post(self): #login
        hasher = sha256()
        hasher.update(request.headers.get("password").encode("UTF-8"))
        username = request.headers.get("username")
        password = hasher.hexdigest()

        #Password cannot be spoofed by timing attack in this case
        if (username in db.user_data and bad_compare(db.user_auths[username], password)):
            db.user_sessions[username] = token_hex(16) #128 bit hex string
            return db.user_sessions[username]
        else:
            return "Invalid username/password"

    
    def get(self):
        username = request.headers.get("username")
        session_key = request.headers.get("session_key")

        #Session key can be spoofed, however
        if bad_compare(db.user_sessions[username], session_key):
            return db.user_data[username]
        else:
            return "Invalid session. Please login."


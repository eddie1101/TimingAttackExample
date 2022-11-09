from flask_restful import Resource, reqparse

from hashlib import sha256
from secrets import token_hex

from bad_compare import bad_compare
from bad_db import db

class UserAPIEndpoint(Resource):

    def __init__(self, *args, **kwargs):
        super(UserAPIEndpoint, self).__init__(*args, **kwargs)


    def post(self): #login

        request_parser = reqparse.RequestParser()
        request_parser.add_argument("username")
        request_parser.add_argument("password")
        args = request_parser.parse_args()

        hasher = sha256()
        hasher.update(args["password"].encode("UTF-8"))
        username = args["username"]
        password = hasher.hexdigest()

        #Password cannot be spoofed by timing attack in this case
        if (username in db.user_data and bad_compare(db.user_auths[username], password)):
            db.user_sessions[username] = token_hex(16) #128 bit hex string
            return db.user_sessions[username]
        else:
            return "Invalid username/password"

    
    def get(self):

        request_parser = reqparse.RequestParser()
        request_parser.add_argument("username")
        request_parser.add_argument("session_key")
        args = request_parser.parse_args()

        username = args["username"]
        session_key = args["session_key"]

        #Session key can be spoofed, however
        if bad_compare(db.user_sessions[username], session_key):
            return db.user_data[username]
        else:
            return "Invalid session. Please login."


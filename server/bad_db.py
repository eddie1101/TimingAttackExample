from hashlib import sha256

#Dictionaries are not a database
class BadDB():

    def __init__(self):
        self.user_auths = {}
        self.user_data = {}
        self.user_sessions = {}

        hasher = sha256()
        hasher.update("example_password".encode("UTF-8"))
        username = "example_username"

        password = hasher.hexdigest()
        self.user_auths[username] = password
        self.user_data[username] = "555-55-5555"

db = BadDB()


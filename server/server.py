from flask import Flask
from flask_restful import Resource, Api

from server_resource import UserAPIEndpoint

app = Flask(__name__)
api = Api(app)

api.add_resource(UserAPIEndpoint, "/user")

if __name__ == "__main__":
    app.run(debug=True)
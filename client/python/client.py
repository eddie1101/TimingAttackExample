import requests

url = "http://127.0.0.1:5000/user"

def get_session_key():
    body = {"username": "example_username", "password": "example_password"}
    return requests.post(url, data=body).json()

if __name__ == "__main__":

    session_key = get_session_key()
    body = {"username": "example_username", "session_key": session_key}
    data = requests.get(url, data=body).json()
    print(data)
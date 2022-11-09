import requests

url = "http://127.0.0.1:5000/user"

def get_session_key():
    post_header = {"username": "example_username", "password": "example_password"}
    return requests.post(url, headers=post_header).json()

if __name__ == "__main__":

    session_key = _get_session_key()
    get_header = {"username": "example_username", "session_key": session_key}
    data = requests.get(url, headers=get_header).json()
    print(data)
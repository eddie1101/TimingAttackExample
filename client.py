import requests

if __name__ == "__main__":

    url = "http://127.0.0.1:5000/user"
    post_header = {"username": "example_username", "password": "example_password"}

    session_key = requests.post(url, headers=post_header).json()
    get_header = {"username": "example_username", "session_key": session_key}
    ssn = requests.get(url, headers=get_header).json()
    print(ssn)
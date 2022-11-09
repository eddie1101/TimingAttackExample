import requests

if __name__ == "__main__":
    response = requests.post("http://127.0.0.1:5000/login", headers={"username": "example_username", "password": "example_password"}).json()
    print(response)
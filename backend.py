import hashlib
import random
import time
import requests
from flask import Flask
from locust import HttpUser, task, between


app = Flask(__name__)

@app.route('/endpoint1')
def endpoint1():
    time.sleep(1)  # Wait for 1 second
    hash_string = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
    return hash_string

@app.route('/endpoint2')
def endpoint2():
    while True:
        response = requests.get('http://localhost:5000/endpoint1')
        hash_string = response.text
        last_character = hash_string[-1]
        
        if last_character.isdigit() and int(last_character) % 2 != 0:
            print(hash_string, "Pass")
            return hash_string + 'Success'
        else:
            if last_character.isdigit() and int(last_character) % 2 == 0:
                print(hash_string, f"`{last_character}` is an even number. Does not pass")
                return hash_string + 'Does not pass'
            elif last_character.isalpha():
                print(hash_string, f"`{last_character}` is a alpabent. Does not pass")
                return hash_string + 'Does not pass'
                

if __name__ == '__main__':
    app.run()


class MyUser(HttpUser):
    wait_time = between(1, 1)  # 1 request per second

    @task
    def endpoint2(self):
        self.client.get('/endpoint2')

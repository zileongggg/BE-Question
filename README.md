README
===================

This repository contains a simple backend code implemented using Python and Flask framework. The code includes two endpoints, `/endpoint1` and `/endpoint2`, which perform certain operations and return responses.

Prerequisites
-------------

Before running the code, make sure you have the following dependencies installed:

*   [Python 3.x](https://www.python.org/)
*   [Flask](https://flask.palletsprojects.com/en/2.3.x/)
*   [Locust](https://locust.io/)

You can install the required Python packages by running the following command:

    pip install flask locust

Usage
-----

To start the backend server, execute the following command:

    python backend.py

This will start the Flask application, and the server will be accessible at `http://localhost:5000`.

### Endpoint 1 - `/endpoint1`

This endpoint performs the following steps:

1.  Waits for 1 second using `time.sleep(1)` function.
2.  Generates a random 256-bit string and computes its SHA-256 hash using `hashlib.sha256`.
3.  Returns the computed hash string as the response.

### Endpoint 2 - `/endpoint2`

This endpoint performs an infinite loop and calls `/endpoint1` internally until a specific condition is met. The steps involved are as follows:

1.  Sends a GET request to `http://localhost:5000/endpoint1` to get the hash string.
2.  Retrieves the last character from the hash string.
3.  Checks if the last character is a digit and if it is an odd number.
4.  If the condition is met, prints the hash string followed by "Pass" and returns the hash string appended with "Success" as the response.
5.  If the condition is not met, prints the hash string followed by "Do not pass" and returns the hash string appended with "Do not pass" as the response.


Load Testing with Locust
-----

To perform the load testing, follow these steps:

1.  Install Locust if you haven't already installed it:

        pip install locust

2.  Start the Locust:
        
        locust -f backend.py

3. Open your browser and navigate to http://localhost:8089 to access the Locust web interface.
4. Set the number of total users, spawn rate, and other parameters as desired.
5. Click the "Start swarming" button to begin the load testing.
6. Note that if you have problems running Locust, make sure the environment path is set.

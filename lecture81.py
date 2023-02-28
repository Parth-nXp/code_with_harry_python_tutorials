'''
Request module: The requests module in Python is a popular HTTP client library that simplifies making HTTP requests in Python. 
It abstracts the complexities of making requests behind a simple API, allowing developers to focus on the logic of their application instead of the underlying networking code.
The requests module provides methods for making different types of HTTP requests such as GET, POST, PUT, DELETE, etc. 
It also supports many features like authentication, cookies, headers, file uploads, timeouts, proxies, etc.
The requests module also supports handling response codes and errors, handling redirects, and handling sessions for making multiple requests to the same server with persistent cookies and authentication information. 
Overall, the requests module is a powerful tool for making HTTP requests in Python.
'''

import requests

# requests.get = requests.get() is a method provided by the Python requests module that allows you to send a GET request to a specified URL and receive the response
r = requests.get("https://financialmodelingprep.com/api/v3/actives")
print(r.text)
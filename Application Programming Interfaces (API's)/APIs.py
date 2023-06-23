# -> What is API's ?
    # An application programming interface (API) is a way for two or more computer programs to communicate with each other.
    # It is a type of software interface, offering a service to other pieces of software.
    # A document or standard that describes how to build or use such a connection or interface is called an API specification.
    # A computer system that meets this standard is said to implement or expose an API.
    # The term API may refer either to the specification or to the implementation.
    
# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects that programmers can use
# create software or interact with an external system.

# Your Program --> API Request --> External System
# Your Program <-- API Response <-- External System

# API returns the output in the form of JSON (JavaScript Object Notation)
# API endpoint is the URL of the API.

# ISS: International Space Station Current Location API -> http://api.open-notify.org/iss-now.json

# requests package is used to fetch the data from API endpoint. It is not an inbuilt package, one need to install this explicitly to use it in their project.

# STATUS CODES:
 
# 1xx: Hold On -> Informational
# 2xx: Here you go...   -> Success
# 3xx: Go Away  -> Redirection
# 4xx: Client Error
# 5xx: Server Error

import requests             # importing requests package (Should be installed using pip)

response = requests.get(url="http://api.open-notify.org/iss-now.json")     # endpoint url is passed as a parameter in requests function and result is stored in response variable.
# So, the response that we get back from the particular API is stored in response variable above.

print(response)     # Response code is printed om the terminal.

print(response.status_code)     # It will print the status code. -> 200 in this case.

response = requests.get(url="http://api.open-notify.org/iss-now.json")       #typo in url
print(response.status_code)     # It will print the status code. -> 404 (FileNotFound Error) in this case. There will be "iss" in place of "is" in the url.

# HTTP status codes: httpstatuses.com

# if response.status_code != 200:         # If response status code is not equal to 200 then,
#     raise Exception("Bad Response from ISS API")
#     print('Error')    
# if response.status_code == 404: # If response status code is 404
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
# The above is the manual way to raise exception.

# We can also use raise_for_status to raise exception:
response.raise_for_status()

# To see the JSON data:
data = response.json()                  # Printing the JSON fetched from API.
print(data)

data = response.json()["message"]       # Printing particular key.
print(data)

data = response.json()["iss_position"]      # Latitude and Longitude will be fetched.
print(data)

longitude = response.json()["iss_position"]["longitude"]     # Longitude will be fetched.
print('Longitude: ', longitude)

latitude = response.json()["iss_position"]["latitude"] # Latitude will be fetched.
print('Latitude: ', latitude)

iss_position = (longitude, latitude)        # Tuple
print(iss_position)

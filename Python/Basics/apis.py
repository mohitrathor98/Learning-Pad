import requests

response = requests.get('http://api.open-notify.org/iss-now.json')

# response codes
# 404: page not found
# 200: success

# Generally
# >100 <200 : hold on, still processing
# >=200 <300 : everything worked fine
# >=300 <400 : Redirectional
# >=400 <500 : You have done something wrong
# >=500 : server issue 
print(response.status_code)
# raises approperiate exception in case of failure
response.raise_for_status()

data = response.json()
print(data)

# API Parameters
# read documentations for correct way

# this dictionary contains all the required
# parameters required for api call
parameters = {
    "lat": 27.2046,
    "lng": 77.4977,
    "formatted": 0
}

# params takes a dictionary of parameters
response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

sunrise = response.json()['results']['sunrise']
print(sunrise) # gives in UTC
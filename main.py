import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "41af627a6b69084a6e7f4b66b7a07f0a"  #make your own API through Openweather
account_sid = "ACe199b20b55f4b38c5d45a306c8f78435"  #Can be found in twilio
auth_token = "321ac57249057eb659706e4ddabdf7aa"  #Can be found in twilio
twilio_number = "+15672882642"  #make your own number through twilio

parameters = {
    "lat": 23.798892,  #current location
    "lon": 90.431633,
    "appid": api_key,
}
response = requests.get(OWM_Endpoint, params=parameters)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
weather_slice = weather_data["list"][:4]   #Takes 12 hours data
will_rain = False
for three_hourly_data in weather_slice:
    condition_code = three_hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It can rain, So bring a Umbrella tomorrow ☔",
        from_=twilio_number,
        to="+8801722382459",
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Sky seems clear",
        from_=twilio_number,
        to="Your phone number",
    )
    print(message.status)

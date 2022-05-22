import requests
from twilio.rest import Client

Own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "6433f59685957411c952b98af9ef38ce"

account_sid = os.environ["AC7aa5d1163a6a8ba8e11d2f3191b51886"]
auth_token = os.environ["03e9b101aa9936fb0808e79f08f2dcee"]


weather_condition = {
    "lat": 54.418289,
    "lon": 26.526859,
    "appid": api_key,
    "exclude": "current,minutely,daily,"
}

response_code = requests.get(Own_endpoint, params=weather_condition)
response_code.raise_for_status()
data = response_code.json()
# rain_data = data["hourly"][0]["weather"][0]["id"]
weather_slice = data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="it's going to rain today. Remember to bring an Umbrella",
        from_='virtual number',
        to='receiver number'
    )

    print(message.sid)





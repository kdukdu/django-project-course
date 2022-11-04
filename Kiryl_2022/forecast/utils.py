import requests

WEATHER_TOKEN = '2fd6d5c272d1eef15c8baff08893c4fa'


def get_weather_info(city: str):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_TOKEN}').json()

    if response['cod'] == '404':
        return None
    else:
        name = response['name']
        temperature = round(response['main']['temp'])
        icon = response['weather'][0]['icon']

    context = {
        'name': name,
        'temperature': temperature,
        'icon': icon
    }
    return context

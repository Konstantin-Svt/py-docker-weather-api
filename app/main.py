import os

import requests


CITY_NAME = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather(city_name: str, api_key: str) -> None:
    if not api_key:
        raise ValueError("API key not provided")

    data = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={
            "key": api_key,
            "q": city_name,
        },
    ).json()
    result = (
        f"{data.get('location').get('name')}/"
        f"{data.get('location').get('country')} "
        f"{data.get('location').get('localtime')} "
        f"Weather: {data.get('current').get('temp_c')} "
        f"Celsius, {data.get('current').get('condition').get('text')}"
    )
    print(result)


if __name__ == "__main__":
    get_weather(CITY_NAME, API_KEY)

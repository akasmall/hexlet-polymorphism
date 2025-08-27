import argparse
import requests
from weather_service import WeatherService


def main(city_name):
    # BEGIN (write your solution here)
    http_client = requests
    weather_service = WeatherService(http_client)

    try:
        data = weather_service.look_up(city_name)
        temperature = data['temperature']
        return f"Temperature in {city_name}: {temperature}C"
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return f"Invalid response format for city: {city_name}"
    # END


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    print(main(args.city))

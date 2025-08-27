API_URL = 'http://localhost:8080/api/v2/'


class WeatherService():
    # BEGIN (write your solution here)
    def __init__(self, http_client):
        self.http_client = http_client
        self.base_url = API_URL

    def look_up(self, city_name):
        url = f"{self.base_url}cities/{city_name}"
        response = self.http_client.get(url)
        response.raise_for_status()
        return response.json()

    # END

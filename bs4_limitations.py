import requests
from bs4 import BeautifulSoup

def scrape_weather_with_bs(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Attempt to find elements that contain weather data
            # (These selectors will likely fail to find the dynamic content)
            temperature = soup.find('span', {'data-testid': 'TemperatureValue'})
            condition = soup.find('div', {'data-testid': 'wxPhrase'})

            if temperature and condition:
                return temperature.text, condition.text
            else:
                return "Data not found", "Data not found"
        else:
            return "Failed to load page", "Failed to load page"
    except Exception as e:
        return f"Error occurred: {e}", "Error occurred"

# Example usage
url = 'https://weather.com/'
temperature, condition = scrape_weather_with_bs(url)
print(f"Weather in New York: {temperature}, {condition}")

import requests
from bs4 import BeautifulSoup

def scrape_weather_with_bs(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print("page content")
            print(soup)
        else:
            return "Failed to load page", "Failed to load page"
    except Exception as e:
        return f"Error occurred: {e}", "Error occurred"

# Example usage
url = 'https://jsonplaceholder.typicode.com'
print(scrape_weather_with_bs(url))

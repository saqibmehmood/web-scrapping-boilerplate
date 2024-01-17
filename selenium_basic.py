from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the WebDriver for Chrome
# ChromeDriverManager automatically downloads the driver binary and sets the path
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_weather(location):
    try:
        # Open the weather.com homepage
        driver.get("https://www.weather.com/")

        # Wait for the page to load (not the best practice, explained later)
        time.sleep(3)

        # Locate the search box element by its ID and input the location
        # 'find_element' is used to find the first element matching the given locator
        search_box = driver.find_element(By.ID, "LocationSearch_input")
        search_box.clear()  # Clear any pre-filled text in the search box
        search_box.send_keys(location)  # Type the location into the search box
        search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

        # Wait for search results to load (again, not the best practice)
        time.sleep(3)

        # Extract weather data using XPath selectors
        # 'find_element' returns the first matching element for the given XPath
        # '.text' is used to get the text content of the found elements
        # Adjust XPaths if the website structure changes
        temperature = driver.find_element(By.XPATH, '//span[@data-testid="TemperatureValue"]').text
        condition = driver.find_element(By.XPATH, '//div[@data-testid="wxPhrase"]').text

        return temperature, condition
    except Exception as e:
        # Print any errors encountered
        print(f"Error occurred: {e}")
        return None
    finally:
        # Close the browser window
        driver.quit()

# Example usage of the function
# location = "New York"
location = "Lahore"
weather_data = get_weather(location)

# Check if data was successfully retrieved and print it
if weather_data:
    temperature, condition = weather_data
    print(f"Weather in {location}: {temperature}, {condition}")
else:
    print("Failed to retrieve weather data.")

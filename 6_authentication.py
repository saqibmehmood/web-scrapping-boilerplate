import requests
from bs4 import BeautifulSoup

# Authentication details
login_url = 'https://example.com/login'
username = 'your_username'
password = 'your_password'

# Create a session to persist the login state
session = requests.Session()

# Send a GET request to the login page to get the necessary tokens or cookies
login_page = session.get(login_url)

# Extract any required tokens or cookies from the login page
# For example, you might need to find a CSRF token from the login form
soup = BeautifulSoup(login_page.content, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Prepare login data
login_data = {
    'username': username,
    'password': password,
    'csrf_token': csrf_token,
}

# Send a POST request to the login endpoint with the login data
response = session.post(login_url, data=login_data)

# Check if login was successful (you may need to customize this check based on the website's response)
if response.ok:
    # Now you can make authenticated requests
    # For example, let's scrape data from a protected page
    protected_page = session.get('https://example.com/protected_page')

    # Parse and extract data from the protected page using Beautiful Soup
    protected_soup = BeautifulSoup(protected_page.content, 'html.parser')
    # Add your scraping logic here

    # Close the session when done
    session.close()
else:
    print('Login failed.')


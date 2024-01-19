import requests
from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/'


# Function to parse a single page and extract book details
def parse_page():
    # Send HTTP request
    response = requests.get(url)
    # Check if the request was successful
    i = 0
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract data for each book
        books = soup.find_all('article', class_='product_pod')

        for book in books:

            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()
            print("product: ", i)
            print("title: ", title)
            print("price: ", price)
            print("title: ", title)
            i += 1
            print("########################################################")
    else:
        print('Failed to retrieve the webpage')

parse_page()
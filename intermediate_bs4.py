import requests
from bs4 import BeautifulSoup
from proxies_list import get_proxy
# Function to parse a single page and extract book details


def send_request(url, proxy, timeout=5, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=timeout)
            return response
        except (requests.exceptions.ProxyError, requests.exceptions.Timeout):
            print(f'Proxy {proxy} failed. Retrying with a different proxy...')
            proxy = get_proxy()
            retries += 1
    return None
def parse_page(soup):
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        print(f'Title: {title}, Price: {price}, Availability: {availability}')

# Function to get the total number of pages
def get_total_pages(soup):
    pagination = soup.find('ul', class_='pager')
    if pagination:
        last_page = pagination.find_all('li', class_='current')[-1].get_text(strip=True)
        total_pages = int(last_page.split('of')[-1].strip())
        return total_pages
    return 1

# Function to scrape the bookstore
def scrap_bookstore(base_url):
    # Send an initial request to get the total number of pages
    initial_response = requests.get(base_url.format(1))
    if initial_response.status_code == 200:
        initial_soup = BeautifulSoup(initial_response.text, 'html.parser')
        total_pages = get_total_pages(initial_soup)

        # Loop through all pages
        for page in range(1, total_pages + 1):
            proxy = get_proxy()
            try:
                response = send_request(base_url.format(page), proxy)
                print("proxy: ", proxy)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    print("###################################################")
                    print("page: ", page)
                    parse_page(soup)
            except:
                page -= 1
                proxy = get_proxy()
    else:
        print('Failed to retrieve the initial webpage')
# Base URL of the website
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Start scraping
scrap_bookstore(base_url)

import random

import requests
from bs4 import BeautifulSoup

def get_proxy():
    proxies = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='table-striped')
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skipping the header row
                columns = row.find_all('td')
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                proxies.append(f'http://{ip}:{port}')
        # return proxies
        return random.choice(proxies)
    except Exception as e:
        print(f'Error occurred: {e}')
        return []
# URL of the proxy website
url = 'https://free-proxy-list.net/'
proxy_list = get_proxy()
print(proxy_list)

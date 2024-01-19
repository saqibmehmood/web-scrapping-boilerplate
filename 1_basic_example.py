from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Web Page</title>
</head>
<body>
    <h1>Welcome to Our Sample Web Page</h1>
    <p>This is a paragraph about web scraping.</p>
    <p>This is another paragraph with <a href="https://example.com">a link</a>.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    
    <p id="test">I am a testing paragraph</p>
    
    <ul>
        <li class="test2">Item 1 with class</li>
        <li class="test2">Item 2 with class</li>
        <li class="test2">Item 3 with class</li>
    </ul>
    
</body>
</html>
"""

# Using Beautiful Soup to parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

print(soup)



# # Extracting and printing the title
# title = soup.find('title').text
# print("Title of the page:", title)
#
# heading = soup.find('h1').text
# print("heading of the page:", heading)
#
# li_tags = soup.find_all('li')
# for li_tag in li_tags:
#     print(li_tag.text)
# # Extracting and printing the text of the first paragraph
# first_paragraph = soup.find('p').text
# print("First paragraph:", first_paragraph)
#
# heading = soup.find("h1").text
# print("heading: ", heading)
#
# # Extracting and printing all paragraphs
# all_paragraphs = soup.find_all('p')
# for para in all_paragraphs:
#     print("Paragraph:", para.text)
#
# # Extracting and printing all list items
# list_items = soup.find_all('li')
# for item in list_items:
#     print("List item:", item.text)
#
# # Extracting and printing the href attribute of the first link
# first_link = soup.find('a')['href']
# print("First link URL:", first_link)

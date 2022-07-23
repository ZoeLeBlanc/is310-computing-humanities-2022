import bs4
# print(bs4.__version__)

from bs4 import BeautifulSoup
# print(BeautifulSoup)
soup = BeautifulSoup(open("first_page.html"), features="html.parser")

# print(soup.prettify())

## Getting list and links

# print(soup.find_all('h1'))
results = soup.find_all('li')
results_dict = {}
results_dict['dh_tools'] = []
for result in results:
    # print(result)
    result = result.get_text()
    print(result)
    results_dict['dh_tools'].append(result)
    # print(result)

links = soup.find_all('a')

for link in links:
    link_text = link.get_text()
    link = link.get('href')
    results_dict['link_result'] = {'link_text': link_text, 'href': link}
    # print(link, link_text)
print(results_dict)

import requests
response = requests.get("https://humanist.kdl.kcl.ac.uk/")

print(response.status_code)
print(response.headers)
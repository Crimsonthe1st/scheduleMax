from bs4 import BeautifulSoup
import requests

base_url = 'https://catalog.uncg.edu'

data = requests.get(base_url + '/arts-sciences/computer-science/computer-science-bs/#requirementstext').text
soup = BeautifulSoup(data)

courses_find_all = soup.find_all('a', {'class': 'bubblelink code'})

courses = []

for c in courses_find_all:
    print(c)
    title = c['title']
    detail_link = c['href']
    print(title + ' ' + detail_link)
    detail_data = requests.get(base_url + detail_link)
    print(detail_data)
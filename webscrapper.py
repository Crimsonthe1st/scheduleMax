
"""
WEB SCRAPPER PURPOSE:
Major and or minor REQS
Requirements for graduation 
List of all classes for major/minor 

tuple for prereq 2D prereq to req
string array for req
"""

#from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import re

def main():

# SCRAPER IS FED INFORMATION, CLEANS IT AND FORMATS IT
    base_url = 'https://catalog.uncg.edu'

    data = requests.get(base_url + '/arts-sciences/computer-science/computer-science-bs/#requirementstext').text
    soup = BeautifulSoup(data)

    courses_find_all = soup.find_all('a', {'class': 'bubblelink code'})

    courses = []
    req: list[str] = []

    for c in courses_find_all:
        title = c['title']
        detail_link = c['href']
        req.append(title)
    

    txt = "".join(req)
    # print(txt)

    txtSub= re.sub(r"\xa0\s*","", txt)

    if re.search(r"[A-Z]{3}\d{3}",txtSub):
        txtCLEAN = re.findall(r"[A-Z]{3}\d{3}", txtSub)
        print(txtCLEAN)


# REGEX TEST PASSED 
            # cleanTXT = "CSC 607"
            # search = re.match(r"CSC\s\d\d\d", cleanTXT)
            # print(search)

if __name__ == "__main__":
    main()
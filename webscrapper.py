
"""
WEB SCRAPPER PURPOSE:
Major and or minor REQS
Requirements for graduation 
List of all classes for major/minor 
"""

#from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
# import re

def main():
    #with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        # page = browser.new_page()
        # try:
        #     page.goto("https://catalog.uncg.edu/arts-sciences/computer-science/computer-science-bs/#requirementstext")
        # except:
        #     print("Error")

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
    txt.replace("\\xa0","")
    print(txt)

# SCRAPER IS FED INFORMATION AND TABLES IT

    # print(tableAsTXT)
    # txt = "".join(tableAsTXT)
    # cleanTXT = txt.replace("\\xa0"," ")
    # print(cleanTXT)
    # garbage: list[str] = []

    # cleaned = cleanTXT.split(",")
    # for c in cleaned:
    #     if(c != r"CSC\s\d\d\d"):
    #         garbage.append(c)

    #     # search = re.match(r"CSC\s\d\d\d", cleanTXT)
    #     print("This is garbage: " , garbage)
    #     print("This is cleaned: " , cleaned)
    #     cleaned = list(set(cleaned)-set(garbage))
    #     print(cleaned)

# REGEX TEST PASSED 
            # cleanTXT = "CSC 607"
            # search = re.match(r"CSC\s\d\d\d", cleanTXT)
            # print(search)

if __name__ == "__main__":
    main()

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
import string

def main():

# SCRAPER IS FED INFORMATION, CLEANS IT AND FORMATS IT
    base_url = 'https://catalog.uncg.edu'

    data = requests.get(base_url + '/arts-sciences/computer-science/computer-science-bs/#requirementstext').text
    soup = BeautifulSoup(data)

# good soup :)
    courses_find_all = soup.find_all('a', {'class': 'bubblelink code'})
    course_name_all = soup.find_all('tr')
    

# SCRAPE FOR COURSE CODES AND FORMAT IT FOR INPUT
    req: list[str] = []

    for c in courses_find_all:
        title = c['title']
        detail_link = c['href']
        req.append(title)
    
    txt = "".join(req)
    txtSub= re.sub(r"\xa0\s*","", txt)

    if re.search(r"[A-Z]{3}\d{3}",txtSub):
        ALL = re.findall(r"[A-Z]{3}\d{3}", txtSub)
        CSC = re.findall(r"CSC\d{3}", txtSub)
        NCSC = list(set(ALL)- set(CSC))

# SCRAPE FOR COURSE NAMES AND FORMAT IT FOR INPUT
    # list was too small for the str? calls too much data from td
    courseTRANS: list[str] = []
    courseIN = ''
    courseOV = ''

    for n in course_name_all:
        name = n
        if(len(courseIN) >= 10000):
            courseOV = courseOV + str(n)
        else:
            courseIN = courseIN + str(n)
        
    if re.search(r'<td>.{1,43}</td>', courseIN):
        part1 = re.findall(r'<td>.{1,43}</td>', courseIN) #43 chars is the longest title
        part2 = re.findall(r'<td>.{1,43}</td>', courseOV)

    courses = part1 + part2
    courseSub = "".join(courses)
    courseSub = courseSub.replace("\n", "").replace("\r", "")

    courseTitles= re.sub(r'<td class="hourscol"></td>',"", courseSub)
    courseTitles= re.sub(r'<sup>.*?</sup>',"", courseTitles)
    courseTitles= re.sub(r'<td="hourscol">',"", courseTitles)
    courseTitles= re.sub(r'<td>',"", courseTitles)

    print(courseTitles)
    parsedTitles = courseTitles.split('</td>')
    courseTitleFiltered = list(filter(None, parsedTitles))
    print(courseTitleFiltered)

 

if __name__ == "__main__":
    main()
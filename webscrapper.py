
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
    REQ: list[str] = []

    for c in courses_find_all:
        title = c['title']
        detail_link = c['href']
        
        # pre-reqs
        detail_data = requests.get(base_url + detail_link).text
        detail_soup = BeautifulSoup(detail_data)
        detail_sec = detail_soup.find('p', {'class': 'courseblockextra noindent'})
        prereqs = []
        if detail_sec is not None:
            detail_find_all = detail_sec.find_all('a', {'class': 'bubblelink code'})
            for s in detail_find_all:
                detail_title = s['title']
                detail_title = re.sub(r"\xa0\s*","", detail_title)
                prereqs.append(detail_title)
                
        # print(prereqs)
        REQ.append(title)
    
    txt = "".join(REQ)
    txtSub= re.sub(r"\xa0\s*","", txt)

    if re.search(r"[A-Z]{3}\d{3}",txtSub):
        ALL = re.findall(r"[A-Z]{3}\d{3}", txtSub)
        CSC = re.findall(r"CSC\d{3}", txtSub)
        NCSC = list(set(ALL)- set(CSC))
    del REQ[:]

    for r in range(13):
        if(req)
        REQ.append(ALL[r])
        print(REQ)
    print(set(ALL))
    print("REQS FOR CSC")

    # print(set(REQ.sort()))
    

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

    # print(courseTitles)
    parsedTitles = courseTitles.split('</td>')
    courseTitleFiltered = list(filter(None, parsedTitles))
    # print(courseTitleFiltered)

    AllTitle = courseTitleFiltered
    TCSC: list[str] = []

    LCSC = len(CSC)
    for i in range(LCSC+1):
        TCSC.append(AllTitle[i])
    # print(AllTitle)
    
    AllNCSC: list[str] = []
    AllNCSC = list(set(AllTitle)- set(TCSC))
    # print(AllNCSC)

    
if __name__ == "__main__":
    main()
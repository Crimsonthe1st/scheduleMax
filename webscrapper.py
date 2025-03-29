
"""
WEB SCRAPPER PURPOSE:
Major and or minor REQS
Requirements for graduation 
List of all classes for major/minor 
"""

from playwright.sync_api import sync_playwright
import re

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            page.goto("https://catalog.uncg.edu/arts-sciences/computer-science/computer-science-bs/#requirementstext")
        except:
            print("Error")

        page.wait_for_timeout(7000)

        table = page.get_by_role('link').all()
        tableAsTXT: list[str] = []
        for t in table:
            tableAsTXT.append(str(table))
        
        txt = "".join(tableAsTXT)

        search = re.match("CSC....", txt)
        print(search)
 
        # for table in tables:
        #     classes = page.getByText(search)
        #     if len(classes) == 1:
        #         print(classes[0])

if __name__ == "__main__":
    main()
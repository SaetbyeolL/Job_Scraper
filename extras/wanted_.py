# Scraping a dynamic website
# Scraping a 'wanted' website job postings based on the keywords entered by the user, extracting relevant details, and saving them to a CSV file named after the keyword


from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv


class Wanted_JobScraper:
    
    def __init__(self, keyword):
        self.keyword = keyword
        self.playwright = sync_playwright().start()                     
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()                            
        self.all_jobs = []
        
    
    def Wanted_scrape_jobs(self):
        self.page.goto("https://www.wanted.co.kr")
        time.sleep(1)                                        
        self.page.click("button.Aside_searchButton__Xhqq3")  
        time.sleep(1.5)
        self.page.query_selector("input.SearchInput_SearchInput__gySrv").fill(self.keyword)
        time.sleep(1.5)
        self.page.keyboard.down("Enter")
        time.sleep(1.5)
        self.page.click("a#search_tab_position")             

        for _ in range(5):                                   
            time.sleep(1)
            self.page.keyboard.down("End")

        self.content = self.page.content()                   
        self.playwright.stop()                              

    
    def Wanted_scrape_page(self):
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")

        for job in jobs:
            title = job.find("strong", "JobCard_title__ddkwM").text
            company = job.find("span", class_="JobCard_companyName__vZMqJ").text
            URL = f"https://www.wanted.co.kr{job.find('a')['href']}"
            job_data = {
                "title": title,
                "company": company,
                "location": "South Korea",
                "URL": URL
            }
            self.all_jobs.append(job_data)

    
    def Wanted_save_to_csv(self):
        file = open(f"{self.keyword}.csv", "w", encoding="utf-8", newline='')  
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Link"])    
        
        for job in self.all_jobs:
            writer.writerow(job.values())  
        file.close()


# execute codes
keyword = input("Please enter a keyword to search for jobs: ")
Wanted = Wanted_JobScraper(keyword)
Wanted.Wanted_scrape_jobs()
Wanted.Wanted_scrape_page()
Wanted.Wanted_save_to_csv()
    

































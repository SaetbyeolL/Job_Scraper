from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time


class Wanted_JobScraper:
    
    def __init__(self):
        self.playwright = sync_playwright().start()                 
        self.browser = self.playwright.chromium.launch(headless=False)  
        self.page = self.browser.new_page()                             
        self.all_jobs = []

    
    def Wanted_scrape_jobs(self, keyword):
        self.page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
     
        for _ in range(5):                                  
            self.page.keyboard.down("End")
            time.sleep(0.1)
            
        self.content = self.page.content()
        self.Wanted_scrape_page()        

        
    def Wanted_scrape_page(self):
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")  

        for job in jobs:
            title = job.find("strong", "JobCard_title__ddkwM").text
            company = job.find("span", class_="JobCard_companyName__vZMqJ").text
            location = job.find("span", class_="JobCard_location__2EOr5").text
            URL = f"https://www.wanted.co.kr{job.find('a')['href']}"
            
            job_data = {
                "title": title,
                "company": company,
                "location": location,
                "URL": URL
            }
            self.all_jobs.append(job_data)
        
        return self.all_jobs
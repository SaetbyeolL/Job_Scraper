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
        self.jobs_posting = []
        
    
    def Wanted_scrape_jobs(self, keyword):
        self.page.goto("https://www.wanted.co.kr/search?query={self.keyword}&tab=position")
     
        for _ in range(5):                                  
            self.page.keyboard.down("End")
            
        self.content = self.page.content()
        self.Wanted_scrape_page()        

    
    def Wanted_scrape_page(self):
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")  

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", "JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            location = job.find("span", class_="JobCard_location__2EOr5").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text
            
            job_info = {
                "title": title,
                "company_name": company_name,
                "location": location,
                "reward": reward,
                "link": link
            }
            self.jobs_posting.append(job_info)
        
        return self.jobs_posting





#########################################################################################
# Keywords for searching job information related to the relevant skill
# keywords = [
#     "flutter",
#     "python",
#     "golang"
# ]


# execute codes
# for keyword in keywords:
#     Wanted = Wanted_JobScraper(keyword)
#     Wanted.Wanted_scrape_jobs()
#     Wanted.Wanted_scrape_page()
#     Wanted.Wanted_save_to_csv()
    
    
Wanted = Wanted_JobScraper(keyword)
Wanted.Wanted_scrape_jobs()
# Wanted.Wanted_scrape_page()










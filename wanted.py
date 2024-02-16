from playwright.sync_api import sync_playwright  # Tools for testing and automating web applications
from bs4 import BeautifulSoup
import time
import csv


class Wanted_JobScraper:
    
    def __init__(self, keyword):
        self.keyword = keyword
        self.playwright = sync_playwright().start()                     # sync_playwright initialize
        self.browser = self.playwright.chromium.launch(headless=False)  # browser initialize, headless: state of being invisible
        # keyword argument: identified by its parameter name. position doesn't matter(ex. launch(headless = False))
        # positional argument: passed based on its position in the function call. when amount of arguments is small. position matters
        self.page = self.browser.new_page()                             # make new browser page(tap)
        self.jobs_posting = []
        
    
    def Wanted_scrape_jobs(self):
        self.page.goto("https://www.wanted.co.kr")
        time.sleep(1)                                        # it makes code execute after designated time.
        self.page.click("button.Aside_searchButton__Xhqq3")  # html_tag.class
        time.sleep(1)
        self.page.query_selector("input.SearchInput_SearchInput__gySrv").fill(self.keyword)
        time.sleep(1)
        self.page.keyboard.down("Enter")
        time.sleep(1)
        self.page.click("a#search_tab_position")             # tag + id

        for _ in range(5):                                   # 5times page scroll down
            time.sleep(1)
            self.page.keyboard.down("End")

        self.content = self.page.content()                   # scrape html tag
        self.playwright.stop()                               # prevent memory leak

    
    
    def Wanted_scrape_page(self):
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")  # get each job postings

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

    
    
    def Wanted_save_to_csv(self):
        file = open(f"{self.keyword}.csv", "w", encoding="utf-8", newline='')  # it creates file if file does not exist
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Reward", "Link"])    # column names
        
        for job in self.jobs_posting:
            writer.writerow(job.values())  # writerow function return only list. so, we extract only values in dictionary
        file.close()



# Keywords for searching job information related to the relevant skill
keywords = [
    "flutter",
    "python",
    "golang"
]

# execute codes
for keyword in keywords:
    Wanted = Wanted_JobScraper(keyword)
    Wanted.Wanted_scrape_jobs()
    Wanted.Wanted_scrape_page()
    Wanted.Wanted_save_to_csv()
    
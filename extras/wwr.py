# Scraping a static website
# Implementing a web scraper for the Weworkremotely website, which scrapes 'remote full-time' job listings from each page and prints them all


import requests
from bs4 import BeautifulSoup


class Weworkremotely_JobScraper:
    
    def __init__(self):
        self.all_jobs = []
        
        
    def wwr_scrape_jobs(self):
        base_url = "https://weworkremotely.com/remote-full-time-jobs"
        total_pages = self.wwr_get_total_pages(base_url)

        for page_number in range(total_pages):
            page_url = f"{base_url}?page={page_number+1}"
            self.wwr_scrape_page(page_url)  
            
            for job in self.all_jobs:
                self.print_job(job)
            print()
        
        
    def wwr_scrape_page(self, url):
        print(f"Scrapping {url}...")
        response = requests.get(url)  
        soup = BeautifulSoup(response.content, "html.parser", )
        jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

        for job in jobs:  
            title = job.find("span", class_="title").text  
            company, type, location = job.find_all("span", class_="company")
            company = company.text
            type = type.text
            location = location.text
            URL = job.find_all("a")[1].get("href") 
            job_data = {
                "title": title,
                "company": company,
                "type": type,
                "location": location,
                "URL": f"https://weworkremotely.com{URL}"
            }
            self.all_jobs.append(job_data)
        
        
    def wwr_get_total_pages(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        pages = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
        return pages
    
    
    def print_job(self, job):
        print("Title:", job["title"])
        print("Company:", job["company"])
        print("JobType:", job["type"])
        print("Location:", job["location"])
        print("Link:", job["URL"])
        print()



# execute code
Weworkremotely = Weworkremotely_JobScraper()
Weworkremotely.wwr_scrape_jobs()
    
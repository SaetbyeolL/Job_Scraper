import requests
from bs4 import BeautifulSoup


class Web3_JobScraper:
    
    def __init__(self, keyword, title="", company="", location="", URL=""):
        self.keyword = keyword
        self.title = title
        self.company = company
        self.location = location
        self.URL = URL
        self.all_jobs = []
        
    def Web3_scrape_jobs(self, keyword):
        url = f"https://web3.career/{self.keyword}-jobs"
        self.Web3_scrape_pages(url)
        

    def Web3_scrape_pages(self, url):
        response = requests.get(
            url,
            headers= {
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            }
        )
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find_all("tr", class_="table_row")
        all_jobs = []
        
        for job in jobs:
            title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text
            # company = job.find("h3", style="color: white; font-size: 12px;").text
            # location = job.find("a", style="font-size: 12px; color: #d5d3d3;").text
            # URL = f"https://web3.career/{self.keyword}-jobs"

            job_data = {
                "title": title,
                # "company": company,
                # "location": location,
                # "URL": URL
            }
            all_jobs.append(job_data)
        return all_jobs

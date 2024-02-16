import requests
from bs4 import BeautifulSoup


class Remotework_JobScraper:
    
    def __init__(self, title="", company="", location="", URL=""):
        self.title = title
        self.company = company
        self.location = location
        self.URL = URL
        self.all_jobs = [] # list which stores all jobs info
    
    
    def rw_scrape_jobs(self, keywords):
        for keyword in keywords:
            url = f"https://remoteok.com/remote-{keyword}-jobs"
            self.rw_scrape_page(url)
            print(f"Jobs for {keyword}:")
            for job in self.all_jobs:
                print(job)
            print()



    def rw_scrape_page(self, url):
        print(f"Scrapping {url}")
        response = requests.get(
            url,
            headers={
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            }
        )
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

        for job in jobs:
            title = job.find("h2", itemprop="title").text.replace("\n", "")
            company = job.find("h3", itemprop="name").text.replace("\n", "")
            location = job.find("div", class_="location").text.replace("\n", "")
            URL = job.find("a", class_="preventLink")["href"]

            job_data = {
                "title": title,
                "company": company,
                "location": location,
                "URL": f"https://remoteok.com{URL}"
            }
            self.all_jobs.append(job_data)


# skills
keywords = [
    "flutter",
    "python",
    "golang"
]


# execute scrape_jobs
Remotework = Remotework_JobScraper()
Remotework.rw_scrape_jobs(keywords)






import requests
from bs4 import BeautifulSoup

# skills
keywords = [
    "flutter",
    "python",
    "golang"
]
# list which stores all jobs info
all_jobs = []


class Job_Scrapping:
    def __init__(self, title="", company="", location="", URL=""):
        self.title = title,
        self.company = company,
        self.location = location,
        self.URL = URL

    def scrape_page(self, url):
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
            self.title = job.find("h2", itemprop="title").text.replace("\n", "")
            self.company = job.find("h3", itemprop="name").text.replace("\n", "")
            self.location = job.find("div", class_="location").text.replace("\n", "")
            self.URL = job.find("a", class_="preventLink")["href"]

            job_data = {
                "title": self.title,
                "company": self.company,
                "location": self.location,
                "URL": f"https://remoteok.com{self.URL}"
            }
            all_jobs.append(job_data)


scraper = Job_Scrapping()
for keyword in keywords:
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    scraper.scrape_page(url)
    print(all_jobs)









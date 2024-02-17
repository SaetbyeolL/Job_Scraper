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
                print(job)
            print()
        
        
    def wwr_scrape_page(self, url):
        print(f"Scrapping {url}...")
        response = requests.get(url)  # 'response' instance created. info about the response received from the web server
        soup = BeautifulSoup(response.content, "html.parser", )
        jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
        # .find    : It returns first item
        # .find_all: It returns all items list[]

        for job in jobs:  # inside "li" tag
            title = job.find("span", class_="title").text  # extract text inside tag
            company, position, region = job.find_all("span", class_="company")
            # there are 3class with the same name. Assign variable names to each class in order
            # ex) letters = ["a", "b", "c"]
            #     a,b,c = letters <- python automatically assign each of element into variables
            company = company.text
            position = position.text
            region = region.text
            URL = job.find_all("a")[1].get("href")  # []: how to extract attribute value from html tag
            
            job_data = {
                "title": title,
                "company": company,
                "position": position,
                "region": region,
                "url": f"https://weworkremotely.com{URL}"
            }
            self.all_jobs.append(job_data)
        
        
    def wwr_get_total_pages(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        pages = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
        return pages
import requests                 #
from bs4 import BeautifulSoup   #

all_jobs = []


def scrape_page(url):
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
        url = job.find("div", class_="tooltip").next_sibling["href"]  # []: how to extract attribute value from html tag
        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "url": f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)


def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
    return buttons


total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))











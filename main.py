import requests                 # it
from bs4 import BeautifulSoup   # it

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
# .find    : It returns first item
# .find_all: It returns all items list[]

all_jobs=[]

for job in jobs: # inside "li" tag
    title = job.find("span", class_="title").text  # extract text inside tag
    company, position, region = job.find_all("span", class_="company")
# there are 3class with the same name. Assign variable names to each class in order
# ex) letters = ["a", "b", "c"]
#     a,b,c = letters <- python automatically assign each of element into variables

    url = job.find("div", class_="tooltip").next_sibling["href"]  #[]: how to extract attribute value from html tag
    company = company.text
    position = position.text
    region = region.text
    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "url": f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)

print(all_jobs)
















from playwright.sync_api import sync_playwright  # Tools for testing and automating web applications
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()  # sync_playwright initialize

browser = p.chromium.launch(headless=False)  # browser initialize, headless: state of being invisible
# keyword argument: identified by its parameter name. position doesn't matter(ex. launch(headless = False))
# positional argument: passed based on its position in the function call. when amount of arguments is small. position matters(ex. plus(1,1))

page = browser.new_page()  # make new browser page(tap)

page.goto("https://www.wanted.co.kr")

time.sleep(1.5)  # it makes code execute after designated time.

page.click("button.Aside_searchButton__Xhqq3")  # html_tag.class

time.sleep(1.5)

page.query_selector("input.SearchInput_SearchInput__gySrv").fill("flutter")  # search 'flutter' in input

time.sleep(1.5)

page.keyboard.down("Enter")

time.sleep(1.5)

page.click("a#search_tab_position")  # tag + id

for x in range(5):
    time.sleep(1.5)
    page.keyboard.down("End")  # scroll down to the end

content = page.content()

p.stop()  # prevent memory leak

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")  # each job postings

jobs_posting = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", "JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link
    }
    jobs_posting.append(job)

# print(jobs_posting)
# print(len(jobs_posting))


file = open("jobs_posting.csv", "w", encoding="utf-8", newline='')  # it creates file if file does not exist
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Location", "Reward", "Link"])  # firstLow

for job in jobs_posting:
    writer.writerow(job.values())  # writerow function return only list. so, we extract only values in dictionary

file.close()












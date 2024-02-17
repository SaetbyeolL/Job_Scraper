from websites.remoteok import Remoteok_JobScraper
from websites.wanted import Wanted_JobScraper
from file import save_to_file


keyword = input("What do you want to search for?")

remoteok = Remoteok_JobScraper(keyword)
remoteok.rw_scrape_jobs(keyword) 
wanted = Wanted_JobScraper(keyword)
wanted.Wanted_scrape_jobs(keyword)
jobs = remoteok.all_jobs + wanted.all_jobs

save_to_file(keyword, jobs)






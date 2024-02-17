from websites.remoteok import Remoteok_JobScraper
from websites.wwr import Weworkremotely_JobScraper
from websites.wanted import Wanted_JobScraper
from file import save_to_file


keyword = input("What do you want to search for?")

remoteok = Remoteok_JobScraper(keyword)
wwr = Weworkremotely_JobScraper(keyword)
wanted = Wanted_JobScraper(keyword)
jobs = remoteok + wwr + wanted
print(jobs)
# save_to_file(keyword, jobs)


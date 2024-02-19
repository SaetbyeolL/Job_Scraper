from flask import Flask, render_template, request
from websites.remoteok import Remoteok_JobScraper
from websites.wanted import Wanted_JobScraper


app = Flask("JobScraper")

@app.route("/") # decorator: when user visit this page, flask will call function which is located right below 
def home():
    return render_template("home.html", name="nico")
# render_template: flask look inside 'templates'folder and get 'home.html'

@app.route("/search")
def hello():
    keyword = request.args.get("keyword") # request argument(ex.keyword)
    remoteok = Remoteok_JobScraper()
    remoteok.rw_scrape_jobs(keyword)
    wanted = Wanted_JobScraper()
    wanted.Wanted_scrape_jobs(keyword)
    jobs =  remoteok.all_jobs + wanted.all_jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run()





















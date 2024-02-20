from flask import Flask, render_template, request, redirect, send_file
from websites.remoteok import Remoteok_JobScraper
from websites.wanted import Wanted_JobScraper
from file import save_to_file


app = Flask("JobScraper")
database = {} # database will be deleted when server is off. for speed up


@app.route("/") # decorator: when user visit this page, flask will call function which is located right below 
def home():
    return render_template("home.html", name="nico")
# render_template: flask look inside 'templates'folder and get 'home.html'


@app.route("/search")
def search():
    keyword = request.args.get("keyword")     
    
    if keyword == None or keyword == "":      
        return redirect("/")
    if keyword in database:
        jobs = database[keyword]
    else:
        remoteok = Remoteok_JobScraper()
        remoteok.rw_scrape_jobs(keyword)
        wanted = Wanted_JobScraper()
        wanted.Wanted_scrape_jobs(keyword)
        jobs =  remoteok.all_jobs + wanted.all_jobs
        database[keyword] = jobs
        
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in database:
        return redirect(f"/search?keyword={keyword}")
    
    save_to_file(keyword, database[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run()





















import requests
from bs4 import BeautifulSoup
# from Scrapper_SO import get_jobs
from indeed_ import get_job

from flask import Flask, render_template, request, redirect, send_file

from exporter import save_to_file



app = Flask(__name__)

db = {}


@app.route("/")
def home():
    return render_template("username.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    existingJobs = db.get(word)
    if word:
        word = word.lower()
        if existingJobs:
            jobs = existingJobs
        else:
            jobs =  get_job(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs#2.csv")
    except:
        return redirect("/")


if __name__ == '__main__':
    app.run()

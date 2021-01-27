import requests
from bs4 import BeautifulSoup


def get_last_page(url):
    LIMIT = 10
    url = f"https://kr.indeed.com/jobs?q=python&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EB%82%A8%EC%96%91%EC%A3%BC&start={LIMIT}"
    result = requests.get(url)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page
get_last

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")

    if company_anchor is not None:
        company = (str(company_anchor.string))
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("span", {"class": "location"}).string
    job_id = html["data-jk"]
    return dict(title=title, company=company, location=location,
                apply_link=f"https://www.indeed.com/viewjob?jk={job_id}")


def extract_jobs(last_page, url):
    LIMIT = 10
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed > page : {page}")
        result = requests.get(f"{url}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_job(word):
    LIMIT = 10
    url = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs

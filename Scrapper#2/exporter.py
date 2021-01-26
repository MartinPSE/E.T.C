import csv


def save_to_file(jobs):
    file = open("jobs#2.csv", mode='w', encoding="utf-8", newline='')
    writer = csv.writer(file)
    writer.writerow([" Title ", " Company ", " Location ", " Link "])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

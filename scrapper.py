from bs4 import BeautifulSoup
import requests

url = "https://ch-fr.indeed.com/jobs?q=scientific%20developer&start=20&vjk=e52bc9527e4f4b9b"

page = requests.get(url)
doc = BeautifulSoup(page.text,'html.parser')

job_titles = doc.select("[class = resultContent]")
job1 = job_titles[0]
job = job1.h2.a.span.string
company = job1.find_all("span")
print(company[1].string)


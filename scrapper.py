# %%

from bs4 import BeautifulSoup
import requests

url = "https://ch-fr.indeed.com/jobs?q=scientific%20developer&start=20&vjk=e52bc9527e4f4b9b"

page = requests.get(url)
doc = BeautifulSoup(page.text,'html.parser')

job_titles = doc.select("[class = resultContent]")
job1 = job_titles[0]
job = job1.h2.a.span.string
company = job1.find("span", {"class": "companyName"}).a.string

print(job,company)


# %%

page = requests.get(url)
doc = BeautifulSoup(page.text,'html.parser')
offers = doc.select("[class = resultContent]")

class Job_offer:

    def __init__(self,offer):
        self.job = offer.h2.a.span.string
        try :
            self.company = offer.find("span", {"class": "companyName"}).a.string
        except:
            self.company = offer.find("span", {"class": "companyName"}).string

    def __repr__(self):
        return str(self.job)

l = [Job_offer(offer) for offer in offers]
# %%

# %%
import httplib2
from bs4 import BeautifulSoup
import requests

url = "https://ch-fr.indeed.com/jobs?q=scientific%20developer&start=20&vjk=e52bc9527e4f4b9b"
http = httplib2.Http()
status, response = http.request(url)

page = requests.get(url)
doc = BeautifulSoup(response,'html.parser')

job_titles = doc.select("[class = resultContent]")
job1 = job_titles[0]
job = job1.h2.a.span.string
company = job1.find("span", {"class": "companyName"}).a.string

print(job,company)
print(job1.a['href'])


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
def open_offer(offer):
    offer_link = offer.h2.a.attrs['href']
    # page = requests.get(offer_link)
    # doc = BeautifulSoup(page.text,'html.parser')
    print(offer_link)


h = open_offer(job1)
# %%
https://ch.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DPZrTd-yPUicohcXLH9VnJt9SZPXCDvF81ezQFgD-5kCbrPX4LJSy9LjqMoqkcMbjYGU-IP12xHpFYN4Id2DDYQG-t0rqvu-LHldJ5QjouyYt1Pvfqo2lF_IqQOF1uvqqPycfHaigIL-1EBR-t10xggYPOW9K4aFWFG96gmFXQ2RLu3CHdYNzMc7KvkHlxeqHIfA0dZGNdxlBFJOLMcwCqSRjhIXCCnP6SsWALwE3VBLCDtcBxKa-S-VQfoney7WDS_pKGP4zkIGO754fFFeHWnJjr0beX9UgP6LRXbHguxdRA0-YodJSx3eUidV42g3hx6xOc_etHWs0vD14yIx_ZqHhhdbTA0hQ_1YehtTHBco6MHWgmbaXBcPmatkJfUSKW1IAAD29MFgPPj2Wn8H8B06l_k6TUKqZN8Jqr_PYVsuiQ6mL8zzl2wc6BGQzjHqIsLIcndjXeG8aTTeeUeIrP8VioIjlE8ih2D2UN0svpa5bul4pt10z2GFabm-qIeqrWYfxKVsL6ag==&xkcb=SoBi-_M3c91tHnQHmh0LbzkdCdPP&p=0&fvj=1&vjs=3
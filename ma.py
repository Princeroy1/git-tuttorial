import requests
from bs4 import BeautifulSoup

url=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(url,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
 publish_date=job.find('span',class_='sim-posted').span.text
 if 'few' in publish_date:
  company_name=job.find('h3',class_='joblist-comp-name').text
  skill=job.find('span',class_='srp-skills').text.replace(' ','')
  publish_date=job.find('span',class_='sim-posted').text
  job_discription=job.find('ul',class_='list-job-dtl clearfix')
  s=job_discription.find('li').text
  
 print(f"Company Name:{company_name}")
 print(f"Skills:{skill}")
 print(f"Published Date:{publish_date.strip()}")
 print(f" {s}")


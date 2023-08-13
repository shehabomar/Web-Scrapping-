import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []

company_name = []

location_name = []

skills = []

links = []

salary =[]

responsibilities = []

date = []

page_num = 0

# --- Accessing the Website --- #
while True:

    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=pytohn&start={page_num}")

    src = result.content

    soup = BeautifulSoup(src, "lxml")
    
    page_limit = int(soup.find("strong").text)

    if page_num > page_limit // 15:
        break

    # --- Job Titles, Job Skills, Company Names, Location Names --- #

    job_titles = soup.find_all("h2",{"class": "css-m604qf"})

    company_names = soup.find_all("a", {"class":"css-17s97q8"})

    location_names = soup.find_all("span", {"class":"css-5wys0k"})

    job_skills = soup.find_all("div" , {"class" : "css-y4udm8"})

    posted_old = soup.find_all("div",{"class": "css-do6t5g"})

    posted_new = soup.find_all("div" , {"class" : "css-4c4ojb"})

    posted = [*posted_new, *posted_old]


    for i in range(len(job_titles)):

        job_title.append(job_titles[i].text)
    
        links.append(job_titles[i].find("a").attrs['href'])
    
        company_name.append(company_names[i].text)
    
        location_name.append(location_names[i].text)
    
        skills.append(job_skills[i].text)

        date.append(posted[i].text)
   
    page_num += 1     

for link in links:
    
    if link.startswith('/'):  # Check if the link is a relative path
    
        link = 'https://wuzzuf.net' + link  # Prepend the base URL

    result = requests.get(link)
    
    src = result.content
    
    soup = BeautifulSoup(src, 'lxml')
    
    salaries = soup.find("div", {"class" : "matching-requirment-icon-container","data-toggle" : "tooltip", "data-placement":"top"}) 
    
    if salaries is not None:
        
        salary.append(salaries.text)
    
    else:
     
        salary.append("N/A")
    
    requirments = soup.find("span", {"itemprop":"responsibilities"}).ul
    
    respon_text = ""
    
    for i in requirments.find_all("li"):
        
        respon_text += li.text +" | "
    
    reson_text = respon_text[:-2]
    
    responsibilities.append(respon_text)    

file_list = [job_title,company_name,location_name,skills,links,salary, responsibilities, date]

exported = zip_longest(*file_list) # to unpack the list 

with open("/home/omar/Documents/web-scrapping/jobstest.csv", "w") as myfile:

    wr = csv.writer(myfile)
    
    wr.writerow(["job title", "company name", "location","skills","links", "salary", "responsibilities", "date"])
    
    wr.writerows(exported)
    

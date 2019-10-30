import requests
from bs4 import BeautifulSoup
import os
cwd = os.getcwd()
print(cwd)
base_url = "https://freeexampapers.com/exam-papers/IB/Physics/Higher/"
#replace Physics with any subject
month_arr = ["May","Nov"]
for i in range(1999,2018):
    to_append = str(i)+"-"+month_arr[(i+1)%2]
    url = base_url+to_append
    response = requests.get(url)
    soup = BeautifulSoup(response.content,features="lxml")
    links = soup.findAll('a')
    for link in links:
        ignore_arr = ["Name","Last modified","Size","Description","Parent Directory"]
        if link.text not in ignore_arr:
            fin_url = url+"/"+str(link.text)
            print(fin_url)
            r = requests.get(fin_url,stream = True)
            if fin_url.startswith(base_url):
                file_name = fin_url.replace(base_url,'')
            file_name = file_name.replace("/","-")
            with open(cwd+"/"+file_name,"wb") as pdf:
                for chunk in r.iter_content(chunk_size=1024):
                      if chunk:
                        pdf.write(chunk)

from bs4 import BeautifulSoup
import requests 
import json 
import time
import os
print('enter the skill you have ')
user_skill=input(">>>>>")
def find_job(page):
    request_data=requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=P`ython&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&pDate=I&sequence=2&startPage={page}')
    info=BeautifulSoup(markup=request_data.text,features='lxml')
    joblist=info.find_all(name='li',class_="clearfix job-bx wht-shd-bx")
    if os.path.isdir (f'D:\webscrapping\job\{page}'):
        pass   
    else:os.mkdir(f'D:\webscrapping\job\{page}')

    for index,job in enumerate(joblist):
        date_of_post=job.find(name='span',class_='sim-posted').span.text
        if 'few' in date_of_post:
            company_name=job.find(name='h3',class_='joblist-comp-name').text.replace(' ','',)
            key_skill=job.find(name='span',class_='srp-skills').text.replace(' ','')
            if user_skill in key_skill:
                with open (f'job\{page}\{index}.txt','w') as fileOBJ:
                    more_info=job.header.h2.a['href']
                    fileOBJ.write(f'date of issue:{date_of_post.strip()}\n')       
                    fileOBJ.write(f'company:{company_name.strip()}\n')
                    fileOBJ.write(f'skills:{key_skill.strip()}\n')    
                    fileOBJ.write(f'more info:{more_info}\n')
                print(f"saving a file {index}.txt")
    return       



    
    

if __name__=='__main__':
    counter:int 
    for counter in range(1,11):
        find_job(page=counter)
        watiing_time=10
        print("*"*10+'  waiting  'f'{watiing_time}sec  '+'*'*10)
        time.sleep(10)
    
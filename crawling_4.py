import bs4
import urllib.request as url

jobName = input("Search for Job : ")
jobName = jobName.replace(' ','+')
path = "https://www.indeed.co.in/jobs?q="+jobName
response = url.urlopen(path)

page = bs4.BeautifulSoup(response,'lxml')

boxes = page.findAll('div',class_='jobsearch-SerpJobCard')

for i in range(len(boxes)):
    title = boxes[i].find('div',class_='title')
    title = title.text.split()
    print(' '.join(title))
    location = boxes[i].find('div',class_='sjcl')
    location = location.text.split()
    print(' '.join(location))
    sal = boxes[i].find('div',class_='salarySnippet')
    if sal:
        sal = sal.text.split()
        print(' '.join(sal))
    else:
        print("Salary not disclosed...")
    print("*"*40)

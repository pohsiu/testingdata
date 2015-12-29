import requests
from BeautifulSoup import BeautifulSoup
import xlwt
import time

book = xlwt.Workbook(encoding="utf-8")

sheet = book.add_sheet("python sheet")
sheet.write(0, 0, "Title")
sheet.write(0, 1, "URL")


print "Start : %s" % time.ctime()
for i in range(1,10,1):
  r = requests.get("http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Amodelling+balloon&page="+`i`+"&keywords=modelling+balloon&ie=UTF8&qid=1445823428&spIA=B00WEE4PHO")
  r_html= r.text.encode('utf8')
  soup = BeautifulSoup(r_html)
  title = soup.findAll('h2',{'class':'a-size-medium a-color-null s-inline s-access-title a-text-normal'})
  plink = soup.findAll('a',{'class':'a-link-normal a-text-normal'},{'href': True })
  
  index1 = 16*(i-1)
  for k in range(0,len(title)):
    index1 = index1 + 1
    sheet.write(index1,0,title[k].string)
  index2 = 16*(i-1)
  for j in range(0,len(plink),2):
    index2 = index2 + 1
    sheet.write(index2,1,plink[j]['href'])
  time.sleep(5)

print "End : %s" % time.ctime()

book.save("modelling.xls")   

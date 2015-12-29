import requests
from BeautifulSoup import BeautifulSoup
import xlwt

book = xlwt.Workbook(encoding="utf-8")


for i in range(1,49,1):
  sheet = book.add_sheet("python sheet" + `i`)
  sheet.write(0, 0, "Title")
  sheet.write(0, 1, "URL")
  
  r = requests.get("http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Arocket+balloon&page="+`i`+"&keywords=rocket+balloon&ie=UTF8&qid=1445574520&spIA=B00N2ZTOBG,B0006N6USM")
  r_html= r.text.encode('utf8')
  soup = BeautifulSoup(r_html)
  title = soup.findAll('h2',{'class':'a-size-medium a-color-null s-inline s-access-title a-text-normal'})
  plink = soup.findAll('a',{'class':'a-link-normal a-text-normal'},{'href': True })
  
  for k in range(0,len(title)):
    index1 = k+1
    sheet.write(index1,0,title[k].string)
  index2=0
  for j in range(0,len(plink),2):
    index2 = index2+1
    sheet.write(index2,1,plink[j]['href']) 


book.save("rocket.xls")   

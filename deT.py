import requests
from BeautifulSoup import BeautifulSoup
import xlwt
import time

book = xlwt.Workbook(encoding="utf-8")


sheet = book.add_sheet("python sheet")
sheet.write(0, 0, "Title")
sheet.write(0, 1, "URL")

detailsheet = book.add_sheet("detail")
detailsheet.write(0,0,"Title")
detailsheet.write(0,1,"Review")
detailsheet.write(0,2,"Q&A")
detailsheet.write(0,3,"price")

for i in range(1,2,1):
  
  
  r = requests.get("http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Arocket+balloon&page="+`i`+"&keywords=rocket+balloon&ie=UTF8&qid=1445574520&spIA=B00N2ZTOBG,B0006N6USM")
  r_html= r.text.encode('utf8')
  soup = BeautifulSoup(r_html)
  title = soup.findAll('h2',{'class':'a-size-medium a-color-null s-inline s-access-title a-text-normal'})
  plink = soup.findAll('a',{'class':'a-link-normal a-text-normal'},{'href': True })
  
  index2 = 16*(i-1)
  detailIndex = 1
  for j in range(0,len(plink),2):
    index2 = index2+1
    sheet.write(index2,1,plink[j]['href'])
    #sub request
    sub_r = requests.get(plink[j]['href'])
    sub_html = sub_r.text.encode('utf8')
    sub_soup = BeautifulSoup(sub_html)
    #detail info
    de_title = soup.find('span',{'id':'productTitle'},{'class':'a-size-large'}).string
    review = soup.find('span',{'id':'acrCustomerReviewText'},{'class':'a-size-base'}).string
    qa = soup.find('span',{'calss':'a-szie-base'}).string
    price = soup.find('span',{'id':'priceblock_ourprice'},{'class':'a-size-medium a-color-price'}).string
    #write to detail sheet
    detailsheet.write(detailIndex,0,de_title)
    detailsheet.write(detailIndex,1,review)
    detailsheet.write(detailIndex,2,qa)
    detailsheet.write(detailIndex,3,price)
    detailIndex = detailIndex + 1
    
    time.sleep(1)
  time.sleep(5)



book.save("rocket.xls")   
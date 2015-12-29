import pyodbc
import requests
from BeautifulSoup import BeautifulSoup
import time


#===connect to SQL server===
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=P15684-R700-IDS\SQLEXPRESS;DATABASE=CrawlerDB;UID=james;PWD=james123!')
cursor = cnxn.cursor()
cursor.execute('select TOP 10 Asin FROM Amazon')
rows = cursor.fetchall()

for row in rows:
  print row.Asin
  print type(row.Asin)
  r = requests.get("http://www.amazon.com/dp/"+row.Asin)
  r_html= r.text.encode('utf8')
  soup = BeautifulSoup(r_html)

  de_title = soup.find('span',{'id':'productTitle'},{'class':'a-size-large'})
  
  while de_title is None:
    r = requests.get("http://www.amazon.com/dp/"+row.Asin)
    r_html= r.text.encode('utf8')
    soup = BeautifulSoup(r_html)
    de_title = soup.find('span',{'id':'productTitle'},{'class':'a-size-large'})
    time.sleep(2)

  review = soup.find('span',{'id':'acrCustomerReviewText'},{'class':'a-size-base'})
  qa = soup.find('a',{'class':'a-link-normal askATFLink'})
  price = soup.find('span',{'id':'priceblock_ourprice'},{'class':'a-size-medium a-color-price'})
  avail = soup.find('div',{'id':'availability'},{'class':'a-section a-spacing-none'})
  
  #level2 find
  avail2 = avail.find('span')
  
  print de_title.string
  print review.string
  if qa is not None:
    #level2 find
    qa2 = qa.find('span')
    print qa2.string
  if avail2 is None:
    print "Not Available"
  else:
    print avail2.string
  if price is None:
    print "None price"
  else:
    print price.string
    

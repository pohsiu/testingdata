import requests
from BeautifulSoup import BeautifulSoup
import time
import os

r = requests.get("http://www.amazon.com/forum/-/Tx3N1RLXJXBO1W1/ref=ask_ql_ql_al_hza?asin=B000W3XEQM")
r_html= r.text.encode('utf8')
soup = BeautifulSoup(r_html)

qus_title = soup.find('meta',{'name':'title'})
#3for XD in qus_title:
print qus_title['content']


"""
while de_title is None:
  r = requests.get("www.amazon.com/forum/-/Tx3N1RLXJXBO1W1/ref=ask_ql_ql_al_hza?asin=B000W3XEQM")
  r_html= r.text.encode('utf8')
  soup = BeautifulSoup(r_html)
  qus_title = sub_soup.findAll('meta')
  time.sleep(2)

"""
"""
text = soup.find('div',{'id':'productDescription'})

#=== Product Description ===
desc = soup.find('div',{'id':'productDescription'})
if desc is not None:
  description = soup.find('p')
  print description
  if description is not None:
    if description.string is not None:
      print description.string
      sheet.write(index,12,description.string)
    else:
      print description.string
      print "No description1"
  else:
    print "No description2"
else:
  print "No description"
#=== Product Description ===
"""







#review = soup.find('span',{'id':'acrCustomerReviewText'},{'class':'a-size-base'})
#reviewURL = soup.find('a',{'id':'acrCustomerReviewLink'},{'class':'a-link-normal'})
#qa = soup.find('a',{'class':'a-link-normal askATFLink'})
#price = soup.find('span',{'id':'priceblock_ourprice'},{'class':'a-size-medium a-color-price'})
#avail = soup.find('div',{'id':'availability'},{'class':'a-section a-spacing-none'})

#level2 find
#qa2 = qa.find('span')
#avail2 = avail.find('span')


#print de_title.string
#print review.string
#print qa2.string
#print reviewURL['href']



os.system("pause")

#print avail2.string is None
#print avail2.text.encode('utf8') is "In Stock."
#if price is not None:
#  print price.string

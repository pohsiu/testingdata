import requests
from BeautifulSoup import BeautifulSoup
import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Python Sheet 1") 
sheet1.write(0, 0, "Title")
sheet1.write(0, 1, "URL")


r = requests.get("http://www.amazon.co.uk/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Agemar+balloon&page=2&keywords=gemar+balloon&ie=UTF8&qid=1445572781")


r_html= r.text.encode('utf8')

#print r_html





soup = BeautifulSoup(r_html)






print soup

title = soup.findAll('h2',{'class':'a-size-medium a-color-null s-inline s-access-title a-text-normal'})

plink = soup.findAll('a',{'class':'a-link-normal a-text-normal'},{'href': True })





for i in range(0,len(title)):
  index1 = i+1
  sheet1.write(index1,0,title[i].string)

index2=0
for j in range(0,len(plink),2):
  index2 = index2+1
  sheet1.write(index2,1,plink[j]['href'])    
    
book.save("test2.xls") 

"""
for j in (0,6,+1):
  f.write(title[j].string)
  f.write("\t") 
  f.write(plink[j]['href'])
  f.write("\n")
  #j=j+1
  

f.close()
"""
   
"""
print title[0].string
print price[0].string
print plink[0]['href']


"""
"""
alink = soup.findAll('a',{'href': True })
for link in alink:
  print link['href']
"""



"""
print r.status_code
print r.headers['a-color-price']
"""

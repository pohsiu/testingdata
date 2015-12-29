import requests
from BeautifulSoup import BeautifulSoup
import xlwt
sheet1 = book.add_sheet("Python Sheet 1") 


r = requests.get("http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=rocket+balloon")


r_html= r.text.encode('utf8')

#print r_html





soup = BeautifulSoup(r_html)

#f.write(soup)
#f.close()


f= open("test.txt","w")
f.write(r_html)
f.close

print soup

titles = soup.findAll('h2',{'class':'a-size-medium a-color-null s-inline s-access-title a-text-normal'})
#price = soup.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'})
plink = soup.findAll('a',{'class':'a-link-normal a-text-normal'},{'href': True })

print titles
print plink

f = open("OutputT2.txt", "w")



for ti in titles:
  f.write(ti.string)
  f.write("\n")

for pl in plink:
  f.write(pl['href'])
  f.write("\n")
  
f.close()


#f = open("Output5.txt", "w")

#print len(title)


"""
print title
print title[0].string
print plink[0].string

for i in range(0,len(title)):
  print title[i].string
for j in range(0,len(plink)):
  print plink[j].string    
    
  
"""
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

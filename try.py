import requests
from BeautifulSoup import BeautifulSoup
import time
import os

sub_r = requests.get("http://www.amazon.com/forum/-/Tx3OW97BEH2M8J3/ref=ask_ql_ql_al_hza?asin=B00KMSOIGM")
#8663509502")
subr_html= sub_r.text.encode('utf8')
sub_soup = BeautifulSoup(subr_html)



question = sub_soup.find('meta',{'name':'title'})['content'].split('Answers: ')[1]
askerData = sub_soup.find('div',{'class':'cdAuthorInfoBlock'}).text.encode('utf8')
askerD1 = askerData
askerData = askerData.split('asked by')[1]
print askerData
askerData = askerData.split('on ')
print askerData

asker = askerData[len(askerData)-2]
askdate = askerData[len(askerData)-1]
answers = sub_soup.findAll('div',{'class':'cdMessageInfo'})
for each in answers:
  #print "here:"+askerD1
  subAnswer = each.find('span',{'style':'display:block'})
  if subAnswer.text.encode('utf8') is '':
    xcode = subAnswer['id'].split('_')[1]
    subAnswer = each.find('span',{'id':'long_'+xcode})
    answer = subAnswer.text.encode('utf8')
  else: 
    answer = subAnswer.text.encode('utf8')
  Authordata = each.find('div',{'class':'answerAuthor'})
  if Authordata is not None:
    Authordata = Authordata.text.encode('utf8').split('answered on ')
    author = Authordata[0]
    answerDate = Authordata[1].split('&')[0]
                  
  voteinfo = each.find('span',{'class':'votingInfo'})
              
  if voteinfo is not None:
    vote = voteinfo.text.encode('utf8')[0]#.split('.')[0]
  if vote is 'D':
    vote = '0'
  print "----------------"
  print "Question:"+question
  print "Answer:"+answer
  print vote
  print "Writer:"+author
  print "AnswerDate:"+answerDate
  print "Asker:"+asker
  print "AskDate:"+askdate
  print askerData            


"""
if desc is not None:
  #print desc.text.encode('utf8')
  description = desc.find('p')
  print description.find('style') is not None
  print description.text.encode('utf8')
  if description is not None:
    pass
    #clear = description.text.encode('utf8')
    #print clear
    #sheet.write(index,12,clear)
  else:
    print "No description"
"""
#=== Product Description ===








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

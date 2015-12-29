import MySQLdb


db = MySQLdb.connect(host='localhost', user='root',passwd='',db='toy_union')
cursor = db.cursor()

cursor.execute("SELECT Asin From product_category where isout='1' Limit 0,2")
row = cursor.fetchall()

for rows in row:
  print rows[0]
  
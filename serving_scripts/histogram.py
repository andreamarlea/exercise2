#histogram.py

#importing
import sys
import psycopg2

#connect to twitter count DB
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

#create minimum parameter and a maximum parameter
k1 = sys.argv[1]
k2 = sys.argv[2] 

#print words with counts between min and max parameter
cur.execute("select word, count from tweetwordcount where count >= %s and count <= %s order by count desc", (k1, k2))
obs = cur.fetchall()
for ob in obs:
   print ob[0], ": ", ob[1]
conn.commit()

#close the connection
conn.close()
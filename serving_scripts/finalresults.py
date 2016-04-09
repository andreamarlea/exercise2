#finalresults.py

#importing
import sys
import psycopg2

#connect to twitter count DB
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

#If no word is returned, this selects all words, ordered by word in ascending order
if len(sys.argv) == 1:
        cur.execute("select word, count from tweetwordcount order by word")
        obs = cur.fetchall()
        for ob in obs:
           print ob[0], ",", ob[1]
        conn.commit()

#If a word is input, this will output the number of counts
else:
        wordinput = sys.argv[1]
        cur.execute("select * from tweetwordcount where word = %s", [wordinput])
        obs = cur.fetchall()
        for ob in obs:
           print 'Total number of occurences of ', ob[0],': ', ob[1]
        conn.commit()

#close the connection
conn.close()

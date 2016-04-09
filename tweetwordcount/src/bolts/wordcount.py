from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        #self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

		# Use psycopg to interact with Postgres
        conn = psycopg2.connect(database = "tcount", user="postgres", password="pass", host="localhost", port="5432")       
        cur = conn.cursor()
        cur.execute("insert into tweetwordcount (word,count) select %s, 0 where not exists (select word from tweetwordcount where word = %s)", (word,word));
        conn.commit() 
		
        cur.execute("update tweetwordcount set count = %s where word = %s", (self.counts[word],word))        
        conn.commit()
		     
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

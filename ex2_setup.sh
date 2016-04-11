#To run the application, you must first clone the tweetwordcount. 
#This folder has the relevant topology, spout, and bolts.
#Please note that the file has been named tweetwordcount instead of ex2tweetwordcount 
#due to potential hiccups with numeric values in the file name.

#Before running, we start mount our volume so that we can store our data
# If you haven't already, find the location of your volume and mount it 
#fdisk -l 
#mount the volume
#mount /dev/xvdf /data
#cd /data

#Additionally, there is a twittercredentials.py file that needs twitter authentication credentials.

#Let's now make a postgres database to store the data.

#Start Postgres
sh start_postgres.sh 
psql -U postgres

#DB Creation in Postgres (Once it has been started)
CREATE DATABASE tcount;

#Connect to DB
\c tcount

#Create table
 CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY NOT NULL,
       count INT NOT NULL);

#Quit Psql
 \q 

#Change directory and RUN TWEETWORDCOUNT! Party time! 
cd /root/ex2/tweetwordcount
sparse run

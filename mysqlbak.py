#!/usr/bin/python
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump utility.
#
##########################################################

# Import required python libraries
import os
import time
import datetime

# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'password'
DB_NAME = '/usr/local/apache/mysqlbak/dbnames.txt'
#DB_NAME = 'dbname'
BACKUP_PATH = '/usr/local/apache/mysqlbak/'

# Getting current datetime to create seprate backup folder like "2017-01-22".
DATETIME = time.strftime('%Y-%m-%d')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
print "creating backup folder"
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print "checking for databases names file."
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print "Databases file found..."
    print "Starting backup of all dbs listed in file " + DB_NAME
else:
    print "Databases file not found..."
    print "Starting backup of database " + DB_NAME
    multi = 0

# Starting actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")

   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       db = db[:-1]         # deletes extra line
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + "--triggers --routines --events" + " " + db + " > " + TODAYBACKUPPATH + "/" + db + "\.sql"
       os.system(dumpcmd)
       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + "--triggers --routines --events" + " " + db + " > " + TODAYBACKUPPATH + "/" + db + '.sql'
   os.system(dumpcmd)

# Tar database backup
tarcmd = "cd " + BACKUP_PATH + " && " " tar czvf " + DATETIME + ".tar.gz " + DATETIME + "/" + " && " + "rm -rf " + DATETIME + "/"
os.system(tarcmd)

# Remove database backup before 7 date
rmbak7 = "find " + BACKUP_PATH + " -mtime +7 -name \*.tar.gz |xargs rm -rf"
os.system(rmbak7)

# Database backup information to the log
logcmd = "echo 'Backup script completed. Your backup has been create in' " + TODAYBACKUPPATH + ".tar.gz" + ">>/var/log/mysqlbak.log "
os.system(logcmd)


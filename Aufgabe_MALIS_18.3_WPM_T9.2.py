#!/usr/bin/env python
# coding: utf-8

# # Automation of a zip file upload

# In[1]:


import os, time, pathlib, ftplib # necessary classes have to be imported


# In[2]:


path_to_watch = "." # path to watch for new files


# In[3]:


before = dict ([(f, None) for f in os.listdir (path_to_watch)]) # create variable containing all files in the directory


# In[ ]:


while 1: # endless loop
  time.sleep (86400) # wait for X seconds
  after = dict ([(f, None) for f in os.listdir (path_to_watch)]) # after now contains all files currently in the directory
  added = [f for f in after if not f in before] # added now contains all new files in directory
  removed = [f for f in before if not f in after] # not really relevant at the moment
  if added: print "Added: ", ", ".join (added) # output, just to check if new files have been found


# In[15]:


if os.path.isfile (fname): # if new file exists
    print ("file exist!")
fsize=os.stat('filepath')
    def fsizeof_fmt (num, suffix='B'):
    for unit in ['Gi']:
        if abs(num) > 300.0:
        <send an email to ammendol@uni-muenster.de> # send an email to admin
        else:
        <upload file to server>
        filename = "myfile"
        ftp = ftplib.FTP ('ftp.ulbms@zdiginrw.hbz.nrw.de')
        ftp.login ("user name", "password")
        ftp.cwd ('zdiginrwulbms')
        open myfile
        ftp.storlines ('STOR ' + filename, myfile)
        ftp.quit()


# In[ ]:


if upload was succesful # if upload succesful
    <send an email to ammendol@uni-muenster.de> # send email to admin
        for filename in os.listdir(): # delete file locally
        if filename.endswith('.zip'):
        os.unlink
else upload not succesful # if upload was not succesful


# In[1]:


if upload was succesful # if upload succesful
          <send an email to ammendol@uni-muenster.de> # send email to admin
	#			delete file locally
	#		else ... upload not successful
	#			check if upload failed before
	#				if yes:
	#					send e-mail to admin
	#				else ... did not fail before
	#	    			store failure in variable
	#					try again the next day
  #    else
  #    		send e-mail to admin
  
  
  if removed: print "Removed: ", ", ".join (removed) # not really relevant at the moment
  before = after # reset for next check which starts after sleep timer


# In[ ]:





# In[ ]:





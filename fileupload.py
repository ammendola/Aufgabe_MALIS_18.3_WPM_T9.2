import os, time, pathlib, ftplib # necessary classes have to be imported
path_to_watch = "\\ubsvirt93\hbzupload" # path to watch for new files
before = dict ([(f, None) for f in os.listdir (path_to_watch)]) # create variable containing all files in the directory
while 1: # endless loop
  time.sleep (86400) # wait for X seconds
  after = dict ([(f, None) for f in os.listdir (path_to_watch)]) # after now contains all files currently in the directory
  added = [f for f in after if not f in before] # added now contains all new files in directory
  removed = [f for f in before if not f in after] # not really relevant at the moment
  if added: print "Added: ", ", ".join (added) # output, just to check if new files have been found
  
  if os.path.isfile (fname): # if new file exists
  print ("file exist!")
  fsize=os.stat('filepath')
	def fsizeof_fmt (num, suffix='B'):
    	for unit in ['Gi']:
       	if abs(num) > 300.0: # if file < 300 GB
		<send an email to ammendol@uni-muenster.de> # send an email to admin
        else:
        	<upload file to server> # upload file to server
	filename = "myfile"
        ftp = ftplib.FTP ('ftp.ulbms@zdiginrw.hbz.nrw.de')
        ftp.login ("user name", "password")
        ftp.cwd ('zdiginrwulbms')
        open myfile
        ftp.storlines ('STOR ' + filename, myfile)
        ftp.quit()
	
	if FTP.voidcmd ("Transfer completed") # if upload succesful, send email to admin
    		<send an email to ammendol@uni-muenster.de> 
        for filename in os.listdir(): # delete file locally
        if filename.endswith('.zip'):
        os.unlink
	else: # if upload was not succesful, check if upload failed before
		ftplib.error_reply
		if yes # if yes, send e-mail to admin
			<send an email to ammendol@uni-muenster.de>
	else: # else ... did not fail before
		while 2: # store failure in variable
			try again next day # try again the next day
  	else: # send e-mail to admin
	<send an email to ammendol@uni-muenster.de>

  if removed: print "Removed: ", ", ".join (removed) # not really relevant at the moment
  before = after # reset for next check which starts after sleep timer

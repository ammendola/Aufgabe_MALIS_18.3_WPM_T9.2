# necessary classes have to be imported
import os, time, pathlib, ftplib, smtplib

# path to watch for new files
path_to_watch = "\\ubsvirt93\hbzupload"
upload successful = false
listoffaileduploadsfromdaybefore = dict()

def sendmailtoadmin(msg):
	adminaddress = "ammendol@uni-muenster"
	server = smtplib.SMTP('smtp.gmail.com', 587) # connect to mail server			
	server.login("youremailusername", "password") #Next, log in to the server
	msg2send = "
		" + msg # The /n separates the message from the headers
	server.sendmail(adminaddress, adminaddress, msg2send)

# the following function checks if the file is not too big for upload
def filenottoobig(filepath):
	if (of.path.getsize(filepath) < 3000000):
		return true
	else
		return false

def uploadfiletomyserver(filepath):
	try:  
		ftp = FTP('_your_server_address_')  
		ftp.login('_username_', '_password_')  
		with open('myfile.py', 'r') as f:  
			ftp.storbinary('STOR %s' % 'remotefile.py', f)  
		ftp.quit()
		uploadsuccessful = true
	except ftplib.all_errors, e:
		errorcode_string = str(e)  
		print errorcode_string
	

# return true if upload did not fail twice before
def countfailedupload(fname):
	if fname in listoffaileduploadsfromdaybefore:
		return listoffaileduploadsfromdaybefore.get(fname)
	else:
		return 0

# create variable containing all files in the directory
before = dict ([(f, None) for f in os.listdir (path_to_watch)]) 

# endless loop to continuously watch the directory and act upon changes
while 1: 
  time.sleep (86400) # wait for X seconds
  after = dict ([(f, None) for f in os.listdir (path_to_watch)]) # after now contains all files currently in the directory
  added = [f for f in after if not f in before] # added now contains all new files in directory
  removed = [f for f in before if not f in after] # not really relevant at the moment

  if added: print "Added: ", ", ".join (added) # output, just to check if new files have been found

  	for fname in added: # this iterates over all new files which have been found in the directory
		if os.path.isfile (fname): # if new file exists
			print ("file exist!")
			if filenottoobig(fname) and countfailedupload(fname) < 2:
				# upload file to server
				if uploadfiletomyserver(fname):
					sendmailtoadmin("upload of file " + fname + " successful!")
					uploadsuccessful = false # needs to be reset for next upload
					listoffaileduploadsfromdaybefore.pop(fname) # remove successfully uploaded file from list of previous failures
					# TODO delete file locally
				else:
					# upload not successful
					# check if upload failed before
					if failedbefore:
						# set marker to 2 to prevent further uploads (has to be checked befor upload!)
						listoffaileduploadsfromdaybefore['fname'] = 2
						sendmailtoadmin("upload of file " + fname + " failed twice, manual check necessary")
					else:
						# try again next day, but remember this failure
						listoffaileduploadsfromdaybefore['fname'] = 1
			else:
				# TODO send e-mail to admin: file too big for automatic upload
		else:
			# # do nothing, as we're not interested in anything but files
			print (fname + " is no file.")

# es folgt der Abschluss wie bekannt			

if removed: print "Removed: ", ", ".join (removed) # not really relevant at the moment
before = after # reset for next check which starts after sleep timer

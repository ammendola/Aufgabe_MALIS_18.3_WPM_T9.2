# necessary classes have to be imported
import os, time, pathlib, ftplib, smtplib

# path to watch for new files
path_to_watch = "C:/Upload"
path_on_server = "/Neues Verzeichnis"
uploadsuccessful = False
listoffaileduploadsfromdaybefore = dict()
# create variable containing all files in the directory
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

# the following function sends a given message via email
def sendmailtoadmin(msg):
	adminaddress = "ammendol@uni-muenster"
	server = smtplib.SMTP('secmail.uni-muenster.de', 587) # connect to mail server
	server.login("ammendol", "Buckdir99") # log in to the server
	server.sendmail(adminaddress, adminaddress, msg)

# the following function checks if the file is not too big for upload
def filenottoobig(filepath):
	if (os.path.getsize(filepath) < 300000):
		return true
	else:
		return false

def uploadfiletomyserver(filepath):
		ftp = FTP('localhost')  
		ftp.login('test', 'test')  
		with open(filepath, 'r') as f:  
			ftp.storbinary('STOR %s' % path_on_server, f)  
		ftp.quit()
		uploadsuccessful = true

# return true if upload did not fail twice before
def countfailedupload(file):
	if file in listoffaileduploadsfromdaybefore:
		return listoffaileduploadsfromdaybefore.get(file)
	else:
		return 0

# endless loop to continuously watch the directory and act upon changes
while 1: 
	time.sleep (30) # here seconds. Wait for one day (86400)
	after = dict ([(f, None) for f in os.listdir (path_to_watch)]) # after now contains all files currently in the directory
	added = [f for f in after if not f in before] # added now contains all new files in directory

	for fname in added: # this iterates over all new files which have been found in the directory
		if os.path.isfile (fname): # if new file exists
			print ("file " + fname + " exist!")
			if filenottoobig(fname) and countfailedupload(fname) < 2:
				# upload file to server
				if uploadfiletomyserver(fname):
					sendmailtoadmin("upload of file " + fname + " successful!")
					uploadsuccessful = false # to be reset for next upload
					listoffaileduploadsfromdaybefore.pop(fname) # remove successfully uploaded file from list of previous failures
					# delete file locally
					## If file exists, delete it ##
					if os.path.isfile(fname):
						os.remove(fname)
					else:    ## Show an error ##
						print("Error: %s file not found" % fname)
				else:
					# upload not successful
					# check if upload failed before
					if countfailedupload(fname) > 0:
						# set marker to 2 to prevent further uploads (has to be checked before upload!)
						listoffaileduploadsfromdaybefore['fname'] = 2
						sendmailtoadmin("upload of file " + fname + " failed twice, manual check necessary")
					else:
						# try again next day, but remember this failure
						listoffaileduploadsfromdaybefore['fname'] = 1
			else:
				sendmailtoadmin("upload of file " + fname + " file too big for automatic upload")
		else:
			# do nothing, as we're not interested in anything but files
			print (fname + " is no file.")

before = after # reset for next check which starts after sleep timer

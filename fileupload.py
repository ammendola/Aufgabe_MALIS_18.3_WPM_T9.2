import os, time # necessary classes have to be imported
path_to_watch = "." # path to watch for new files
before = dict ([(f, None) for f in os.listdir (path_to_watch)]) # create variable containing all files in the directory
while 1: # endless loop
  time.sleep (30) # wait for X seconds
  after = dict ([(f, None) for f in os.listdir (path_to_watch)]) # after now contains all files currently in the directory
  added = [f for f in after if not f in before] # added now contains all new files in directory
  removed = [f for f in before if not f in after] # not really relevant at the moment
  if added: print "Added: ", ", ".join (added) # output, just to check if new files have been found
  
  # if new file:
  #    if file < 300 GB
  #    		upload file to server
  #			if upload succesful:
  #				send e-mail to admin
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
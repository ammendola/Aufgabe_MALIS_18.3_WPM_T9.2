

import smtplib # ZUSÄTZLICH EINBINDEN FÜR MAILVERSAND

# ab hier zunächst alles wie gehabt

import os, time, pathlib, ftplib # necessary classes have to be imported
path_to_watch = "\\ubsvirt93\hbzupload" # path to watch for new files
before = dict ([(f, None) for f in os.listdir (path_to_watch)]) # create variable containing all files in the directory
while 1: # endless loop
  time.sleep (86400) # wait for X seconds
  after = dict ([(f, None) for f in os.listdir (path_to_watch)]) # after now contains all files currently in the directory
  added = [f for f in after if not f in before] # added now contains all new files in directory
  removed = [f for f in before if not f in after] # not really relevant at the moment
  if added: print "Added: ", ", ".join (added) # output, just to check if new files have been found

Im nächsten Schritt prüfst du hier, ob "fname" eine Datei ist, das ist völlig ok, allerdings hast du "fname" ja gar nicht. Das hast du dir hier gerade ausgedacht. Was du aber hast, ist "added" ... und in "added" stehen alle neuen Dateien drin. (Häufig wird es natürlich nur eine Datei sein. Aber es könnten halt auch zwei oder drei oder noch mehr sein.)

Was du also als nächstes tun musst, ist, für alle Elemente in "added" deine Prüfungen durchzuführen. Das bedeutet: Du musst hier durch das Dictionaly "added" laufen und für jedes enthaltene Element prüfen, ob die Datei zu groß ist etc.

Dazu schau dir am besten mal https://www.python-kurs.eu/dictionaries.php an. Dort werden Dictionaries erklärt und der Abschnitt "Iteration über ein Dictionary" verrät dir, wie du eine Schlefe für dein Dictionary bauen kannst.


	for fname in added: # this iterates over all new files which have been found in the directory
		if os.path.isfile (fname): # if new file exists
			print ("file exist!")
			# HIER PRÜFUNGEN, UPLOAD UND LOKALES LÖSCHEN
		else:
			print (fname + " is no file.")
			server = smtplib.SMTP('smtp.gmail.com', 587) # connect to mail server			
			server.login("youremailusername", "password") #Next, log in to the server
			msg = "
				no file!" # The /n separates the message from the headers
				server.sendmail("ammendol@uni-muenster.de", "ammendol@uni-muenster.de", msg)

# 	Den Rest von deinem Code habe ich noch nicht vollständig geprüft, probier erst einmal, diese Schleife hier zu verstehen und nachzuvollziehen. Und dann solltest du, bevor du weitermachst, es schaffen, Dein Programm wirklich auszuführen und eine E-Mail zu versenden!

# es folgt der Abschluss wie bekannt			

if removed: print "Removed: ", ", ".join (removed) # not really relevant at the moment
before = after # reset for next check which starts after sleep timer
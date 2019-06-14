## Automation of a zip file upload

(see [Aufgabe_MALIS_18.3_WPM_T9.1](https://github.com/ammendola/Aufgabe_MALIS_18.3_WPM_T9.1), Optimierungspotenzial im Workflow)

### [Development in Jupyter Notebook-Script](http://localhost:8888/notebooks/Aufgabe_MALIS_18.3_WPM_T9.2.ipynb):

## First draft

### Check if zip files are in the local directory


```python
from pathlib import Path
```


```python
data_folder = Path("ubsvirt93/hbzupload")
```


```python

# KUF: I don't understand why you do this - this will be exactly the same path,

folder_to_open = data_folder
```


```python

# KUF: "open" open a file - not a folder
# see https://docs.python.org/3/library/functions.html#open

f = open(folder_to_open)
```


```python

# KUF - here you hard code the folder from above again and add
# a file that is not existign (.zip").
# I guess you you want a list of all files in the folder
# see: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

filename = Path("ubsvirt93/hbzupload/.zip")
```


```python

# KUF: Maybe you want to check here if the files all end with ".zip".
# you coudl to this with an if-Statement and the String method "endswith"
# see: https://docs.python.org/3/library/stdtypes.html

print(filename.suffix)
# prints "zip"
```


```python
# KUF: Why?

if not filename exists:
 close(data_folder)
else:
 filename.sort(key=os.path.getmtime)
```

### Open FileZilla and upload zip files to a FileZilla directory


```python

# KUF I don't know why you want to do this. Filezilla is not needed as you 
# will do the upload directly using pythons "ftplib".

import subprocess
p = subprocess.Popen([r"C:\filezilla\programm.exe", "-h"], stdout=subprocess.PIPE)
p.wait()
print p.stdout.read()
```


```python
# KUF I guess this is not really needed.

import shutil
shutil.move('ubsvirt93/hbzupload/Buerener_Zeitung_Film_040.zip', 'filezilla/ulbms/zip')
```

### Connect to ftp server and upload zip files


```python
FTP.connect(host='hbz', port=0, timeout=None, source_address="ftp://ulbms@zdiginrw.hbz.nrw.de")
from ftplib import FTP
    with FTP("ftp://ulbms@zdiginrw.hbz.nrw.de") as ftp:
... ftp.login("user name, password")
... ftp.dir("zip-files")
```


```python
# KUF: I thinks this won't work; rather use the method "cwd"
# see: https://stackoverflow.com/questions/43717984/change-directory-on-server-before-uploading-files-with-ftplib-in-python

cd zdiginrwulbms
```


```python
# KUF: not sure if this is needed.

import shutil
shutil.move('filezilla/ulbms/Buerener_Zeitung_Film_040.zip', 'zdiginrwulbms/Buerener_Zeitung_Film_040.zip')
```

### Delete zip files from the local server


```python
import os
for filename in os.listdir():
    if filename.endswith('.zip'):
        os.unlink(Buerener_Zeitung_Film_040.zip)
```


## Second draft

### Check if zip files are in the local directory


```python

# KUF: Maybe implement this watchin later. After getting 
# the automatic upload done

import os, time
path_to_watch = "."
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (30)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: print "Added: ", ", ".join (added)
  if removed: print "Removed: ", ", ".join (removed)
  before = after
```

### Open FileZilla and upload zip files to a FileZilla directory


```python

# KUF: see aboce - IMO not needed.

import subprocess
p = subprocess.Popen([r"C:\filezilla\programm.exe", "-h"], stdout=subprocess.PIPE)
p.wait()
print p.stdout.read()
```


```python
import shutil
shutil.move('ubsvirt93/hbzupload/Buerener_Zeitung_Film_040.zip', 'filezilla/ulbms/zip')
```

### Connect to ftp server and upload zip files


```python
import ftplib
filename = "Buerener_Zeitung_Film_040.zip"
ftp = ftplib.FTP ('ftp.ulbms@zdiginrw.hbz.nrw.de')
ftp.login ("user name", "password")
ftp.cwd('ulbms@zdiginrw.hbz.nrw.de')
myfile = open ('filezilla/ulbms/Buerener_Zeitung_Film_040.zip', 'rb')
ftp.storlines('STOR ' + filename, myfile)
ftp.quit()
```

### Delete zip files from the local server


```python
import os
for filename in os.listdir():
    if filename.endswith('.zip'):
        os.unlink(Buerener_Zeitung_Film_040.zip)

´´´´

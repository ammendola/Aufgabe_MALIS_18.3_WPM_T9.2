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
folder_to_open = data_folder
```


```python
f = open(folder_to_open)
```


```python
filename = Path("ubsvirt93/hbzupload/.zip")
```


```python
print(filename.suffix)
# prints "zip"
```


```python
if not filename exists:
 close(data_folder)
else:
 filename.sort(key=os.path.getmtime)
```

### Open FileZilla and upload zip files to a FileZilla directory


```python
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
FTP.connect(host='hbz', port=0, timeout=None, source_address="ftp://ulbms@zdiginrw.hbz.nrw.de")
from ftplib import FTP
    with FTP("ftp://ulbms@zdiginrw.hbz.nrw.de") as ftp:
... ftp.login("user name, password")
... ftp.dir("zip-files")
```


```python
cd zdiginrwulbms
```


```python
import shutil
shutil.move('filezilla/ulbms/Buerener_Zeitung_Film_040.zip', 'zdiginrwulbms/Buerener_Zeitung_Film_040.zip')
```

### Delete zip files from the local server


```python
import os
for filename in os.listdir():
    if filename.endswith('.zip'):
        os.unlink(Buerener_Zeitung_Film_040.zip)



### Check if zip files are in the local directory


```python
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

## Open FileZilla and upload zip files to a FileZilla directory


```python
import subprocess
p = subprocess.Popen([r"C:\filezilla\programm.exe", "-h"], stdout=subprocess.PIPE)
p.wait()
print p.stdout.read()
```


```python
import shutil
shutil.move('ubsvirt93/hbzupload/Buerener_Zeitung_Film_040.zip', 'filezilla/ulbms/zip')
```

## Connect to sftp server and upload zip files


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

## Delete zip files from the local server


```python
import os
for filename in os.listdir():
    if filename.endswith('.zip'):
        os.unlink(Buerener_Zeitung_Film_040.zip)



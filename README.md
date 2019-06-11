Automation of a zip file upload
Check if zip files are in the local directory
from pathlib import Path
from pathlib import Path
data_folder = Path("ubsvirt93/hbzupload")
data_folder
folder_to_open = data_folder
f = open(folder_to_open)
ubsvirt93/hbzupload/.zip
filename = Path("ubsvirt93/hbzupload/.zip")
print(filename.suffix)
# prints "zip"
if not filename exists:
 close(data_folder)
else:
 filename.sort(key=os.path.getmtime)
Open FileZilla and upload zip files to a FileZilla directory
import subprocess
p = subprocess.Popen([r"C:\filezilla\programm.exe", "-h"], stdout=subprocess.PIPE)
p.wait()
print p.stdout.read()
move
import shutil
shutil.move('ubsvirt93/hbzupload/Buerener_Zeitung_Film_040.zip', 'filezilla/ulbms/zip')
Connect to sftp server and upload zip files
SFTP.connect(host='hbz', port=0, timeout=None, source_address="sftp://ulbms@zdiginrw.hbz.nrw.de")
from sftplib import SFTP
    with SFTP("sftp://ulbms@zdiginrw.hbz.nrw.de") as sftp:
... sftp.login("user name, password")
... sftp.dir("zip-files")
cd zdiginrwulbms
import shutil
shutil.move('filezilla/ulbms/Buerener_Zeitung_Film_040.zip', 'zdiginrwulbms/Buerener_Zeitung_Film_040.zip')
Delete zip files from the local server
import os
for filename in os.listdir():
    if filename.endswith('.zip'):
        os.unlink(Buerener_Zeitung_Film_040.zip)

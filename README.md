# upload_zip

@echo off
::echo Lokales Verzeichnis öffnen
open X:\\ubsvirt93/hbzupload
::echo Prüfen, ob ZIP-Dateien im lokalen Verzeichnis vorhanden sind
dir.zip
::echo Wenn ja, alle Dateien nach Datum auflisten
ls*.zip
::echo Programm FileZilla öffnen
open filezilla
::echo ZIP-Dateien mit log-Dateien bis max. 300 GB in FileZilla laden
push X:\Buerener_Zeitung_Film_040.zip -->> filezilla
::echo Verbindung zu SFTP-Server aufbauen
open sftp://ulbms@zdiginrw.hbz.nrw.de
benutzername
passwort
::echo Ins Verzeichnis zdiginrwulbms wechseln
cd zdiginrwulbms
::echo ZIP-Dateien hochladen
push Buerener_Zeitung_Film_040.zip
::echo Sobald die Dateien hochgeladen sind, selbige vom lokalen Server löschen
del X:\Buerener_Zeitung_Film_040.zip

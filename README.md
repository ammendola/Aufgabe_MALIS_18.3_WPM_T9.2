## Dokumentation eines automatisierten Upload-Prozesses

Innerhalb eines Digitalisierungsprojektes an der ULB Münster soll der bislang manuell durchgeführte Upload automatisiert werden. Hierfür wurde mit Python ein Code geschrieben, der diesen Prozess startet und folgende Schritte umfasst:

Zunächst wurden die benötigten Klassen/Libraries importiert (os, time, pathlib, ftplib, smtlib) und einige Variablen definiert werden, die für die Umsetzung des Codes wichtig sind, z.B. die Pfade zur Datei und zum Server.

Anschließend wurden verschiedene Funktionen benannt und definiert, um den eigentlichen Code schlank zu halten (Mailversand an den Admin, Größenprüfung der hochzuladenden Datei, Hochladen der Datei auf den FTP-Server, Zählung der fehlgeschlagenen Uploads).

Erst dann beginnt der eigentliche Code mit einer while-Schleife, die das Verzeichnis daraufhin überprüft, ob sich darin Dateien befinden. >Wenn nein, erfolgen keine weiteren Schritte (Code-Zeilen 77-79).
>Wenn ja, wird anhand der Funktion "filenottoobig" geprüft, ob die Datei nicht zu groß ist (kleiner/gleich 300 GB) und ob die Datei kleiner als zweimal nicht hochgeladen werden konnte.
>>Wenn beides zutrifft, wird die Datei auf den Server hochgeladen und es wird eine Mail an den Admin geschickt, dass der Upload erfolgreich war und löscht die Datei sowohl aus der Liste der am Vortag nicht erfolgreich hochgeladenen Dateien (falls sie dort stand) als auch aus dem lokalen Verzeichnis. Wenn der Upload aber nicht erfolgreich war, wird anhand der eingangs definierten Funktion countfailedupload geprüft, ob der Upload schon mehr als einmal fehlgeschlagen ist. Wenn ja, wird eine Mail an den Admin gesendet, dass der Upload zweimal fehlgeschlagen ist und eine manuelle Prüfung notwendig ist. Wenn aber der Upload bislang nur einmal fehlgeschlagen ist, soll der Upload am nächsten Tag wiederholt werden, der fehlgeschlagene Upload soll aber gespeichert werden (= 1), falls er noch einmal fehlschlägt.
>>Wenn nun aber die weiter oben stehende Prüfung, ob die Datei zu groß ist, positiv ausfällt, soll eine entsprechende Mail an den Admin geschickt werden.



Fragen:

Müsste in der Funktion filenotoobig nicht stehen: "fname statt filepath"?

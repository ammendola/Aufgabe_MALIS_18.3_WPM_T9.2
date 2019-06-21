## Dokumentation eines automatisierten Upload-Prozesses

Innerhalb eines Digitalisierungsprojektes an der ULB Münster soll der bislang manuell durchgeführte Vorgang, die Bild-Dateien in das Upload-Verzeichnis hochzuladen, automatisiert werden. Hierfür wurde mit Python ein Skript geschrieben, das genau diesen Vorgang initiiert, sobald Dateien auf dem lokalen Server hochgeladen wurden. Dabei darf die Datenmenge pro Upload-Vorgang allerdings nicht größer als 300 GB sein, damit der Upload in einem nächtlichen Prozess durchlaufen kann und die täglichen Arbeitsprozesse nicht behindert werden.

Zunächst wurden die benötigten Klassen/Libraries importiert (os, time, pathlib, ftplib, smtlib) und einige Variablen definiert werden, die für die Umsetzung des Codes wichtig sind, z.B. die Pfade zur Datei und zum Server oder eine Liste der am Vortag fehlgeschlagenen Uploads (Code-Zeilen 4–10).

Anschließend wurden verschiedene Funktionen benannt und definiert, um den eigentlichen Code schlank zu halten (Mailversand an den Admin, Größenprüfung der hochzuladenden Datei, Hochladen der Datei auf den FTP-Server, Zählung der fehlgeschlagenen Uploads: Code-Zeilen 12–39).

Erst dann beginnt der eigentliche Code mit einer while-Schleife, die das Verzeichnis daraufhin überprüft, ob sich darin Dateien befinden. 

Wenn nein, erfolgen keine weiteren Schritte (Code-Zeilen 74–76), sondern je nach Einstellung des Sleep timers ein regelmäßiger Check des Verzeichnisses (Code-Zeile 78).

Wenn ja, wird anhand der Funktion "filenottoobig" geprüft, ob die Datei nicht zu groß ist (kleiner/gleich 300 GB) und ob die Datei weniger als zweimal nicht hochgeladen werden konnte.

Wenn beides zutrifft, wird die Datei auf den Server hochgeladen und es wird eine Mail an den Admin geschickt, dass der Upload erfolgreich war. Zudem wird die Datei sowohl aus der Liste der am Vortag nicht erfolgreich hochgeladenen Dateien (falls sie dort stand) als auch aus dem lokalen Verzeichnis gelöscht.

>> Wenn der Upload nicht erfolgreich war, wird anhand der eingangs definierten Funktion "countfailedupload" geprüft, ob der Upload schon mehr als einmal fehlgeschlagen ist.

>> Wenn ja, wird eine Mail an den Admin gesendet, dass der Upload zweimal fehlgeschlagen ist und eine manuelle Prüfung notwendig ist.

>> Wenn der Upload bislang nur einmal fehlgeschlagen ist, soll der Upload am nächsten Tag wiederholt werden, der fehlgeschlagene Upload soll aber gespeichert werden (= 1), falls er noch einmal fehlschlägt.

Wenn die Prüfung, ob die Datei zu groß für den automatischen Upload ist (Code-Zeile 73), positiv ausfällt, soll eine entsprechende Mail an den Admin geschickt werden.

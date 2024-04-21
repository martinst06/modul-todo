### Projektarbeit
- Für meinen kleinen Projektarbeit, wollte ich einen Task Manager / To do Liste machen. Bei dem kann man Tasks / Aufgaben erstellen. Diesen Aufgaben kann man an unterschiedlichen Personen unterteilen (User 1, User 2, User 3). Man kann dann diesen Tasks entweder löschen oder fertigstellen nachdem sie erledigt wurden. Man kann dann die erledigten Aufgaben sehen.

### Beschreibung Aussehen
- Ich habe ein Eingabefeld und ein Button “Done". In das Eingabefeld schreibt man einen Aufgabennamen und sobald man auf “Done" drückt, erscheint er als eigene Aufgabe unten in einem Div. Das Div enthält auch einen Button “Done" und einen “Delete". Wenn Sie auf “Done" klicken, werden Sie auf eine andere Seite weitergeleitet. Sie können zu dieser Seite gehen, indem Sie auf dem Button “Finished Tasks" oben links drücken, und Sie werden dorthin weitergeleitet, wo Sie die bereits erledigten Aufgaben sehen können.

### Requirements:
- Visual Studio Code
- Python
- Flask für Python (pip3 install Flask)
- Docker

### Visual Studio Code Extensions
- Docker
- Dev Containers
- Live Server

### Anleitung
Wie startet man das Projekt?
- Mann muss zuerst einen Docker Image aufbauen (build). Man macht das indem man Rechts-Klick auf dem Dockerfile drückt und "Build Image" auswählt und den Image einen sinnvollen Namen geben.
- Danach muss man ins Docker gehen und den Image starten indem man den Image auswählt und "Run Interactive" drückt.
- Dann öffnet sich den Port den man spezifiziert hat ins requirements.txt
- Dann ist die Applikation am laufen!
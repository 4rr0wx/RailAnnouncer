Hier ist eine Beispiel-README-Datei für dein `RailAnnouncer` Programm:


# RailAnnouncer

RailAnnouncer ist ein Python-Programm mit einer grafischen Benutzeroberfläche (GUI), das Text-to-Speech-Ansagen für einen Zugsimulator abspielt. Das Programm verwendet `gtts` für die Text-to-Speech-Funktionalität und `tkinter` für die GUI.

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Dateistruktur](#dateistruktur)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Lizenz](#lizenz)

## Installation

### Voraussetzungen

- Python 3.12.4 oder höher
- pip (Python package installer)

### Benötigte Pakete

Installiere die benötigten Pakete mit pip:

```bash
pip install gtts pygame
```

## Verwendung

1. Starte das Programm:

    ```bash
    python rail_announcer.py
    ```

2. Wähle eine Strecke und einen Zugdienst aus den Dropdown-Menüs.
3. Klicke auf "Nächste Station" oder "Vorherige Station", um durch die Stationen zu navigieren.
4. Die aktuelle und nächste Station werden angezeigt.
5. Die Ansagen werden als "Nächster Halt Next Stop: <Stationsname>" abgespielt.

## Dateistruktur

Stelle sicher, dass deine Ordner- und Dateistruktur wie folgt aussieht:

```
.
├── rail_announcer.py
├── Strecke1
│   ├── Zugdienst1.txt
│   ├── Zugdienst2.txt
├── Strecke2
│   ├── Zugdienst1.txt
│   ├── Zugdienst2.txt
```

Jede `.txt`-Datei sollte eine Liste von Bahnhofsname enthalten, wobei jeder Name in einer neuen Zeile steht.

## Screenshots

Füge hier einige Screenshots deines Programms ein, um den Benutzern einen visuellen Eindruck zu geben.

## Contributing

Beiträge sind willkommen! Bitte eröffne ein Issue, um Fehler zu melden oder neue Features zu diskutieren.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
```

### Hinweise:

- Speichere den oben genannten Inhalt in einer Datei namens `README.md` in deinem Projektverzeichnis.
- Ersetze `rail_announcer.py` durch den tatsächlichen Namen deiner Python-Datei, falls dieser anders ist.
- Füge eventuell Screenshots hinzu, um die Benutzeroberfläche deines Programms zu zeigen.
- Du kannst auch weitere Abschnitte hinzufügen, falls du zusätzliche Informationen bereitstellen möchtest.
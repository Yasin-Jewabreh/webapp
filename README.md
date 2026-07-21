# HelpYourNeighbour

HelpYourNeighbour ist eine webbasierte Vermittlungsplattform, die hilfsbedürftige Menschen mit engagierten Helferinnen und Helfern – insbesondere Studierenden, Schülerinnen und Schülern sowie Auszubildenden – verbindet.

## Features

### Rollen- und Freigabesystem

Die Anwendung unterscheidet zwischen drei Rollen:

- **Pflegebedürftige Person (PP):** Kann einen Hilfsauftrag erstellen, Bewerbungen prüfen, Termine verwalten und mit dem ausgewählten Helfer chatten.
- **Helfer:** Kann offene Aufträge einsehen, sich darauf bewerben, Termine verwalten und mit einer zugeordneten pflegebedürftigen Person chatten.
- **Admin:** Kann neu registrierte Nutzer prüfen, freigeben und deaktivieren.

Nicht freigegebene Nutzer können sich anmelden, erhalten aber noch keinen Zugriff auf die geschützten Funktionen der Plattform.

### Registrierung und Helferprüfung

Bei der Registrierung wird zunächst die gewünschte Rolle ausgewählt.

Helfer müssen zusätzlich:

- einen Vorstellungstext eingeben,
- ein Führungszeugnis als PDF hochladen.

Das Führungszeugnis kann anschließend in der Adminübersicht geprüft werden, bevor der Helfer freigegeben wird.

### Auftrags- und Bewerbungsmanagement

Pflegebedürftige Personen können einen Hilfsauftrag mit ihrer Wohnsituation und einer Beschreibung des Unterstützungsbedarfs erstellen.

Helfer können:

- offene Aufträge einsehen,
- sich auf einen Auftrag bewerben,
- keine doppelte Bewerbung für denselben Auftrag absenden.

Die pflegebedürftige Person kann eingegangene Bewerbungen ansehen und einen Helfer annehmen oder ablehnen.

Erst nach Annahme einer Bewerbung wird der Auftrag dem ausgewählten Helfer zugeordnet.

### Terminverwaltung

Helfer und pflegebedürftige Personen können innerhalb eines angenommenen Auftrags:

- Termine anfragen,
- Termine bestätigen oder ablehnen,
- Termine bearbeiten,
- Termine löschen,
- Termine als erledigt markieren,
- abgeschlossene Termine in der Historie einsehen.

Die Anwendung unterscheidet zwischen:

- bestätigten Terminen,
- offenen Terminanfragen,
- Terminen, bei denen auf die Antwort der anderen Person gewartet wird.

Zusätzlich verhindert eine Überschneidungsprüfung, dass für dieselben Beteiligten gleichzeitig mehrere Termine angelegt werden.

Wird ein Auftrag gelöscht, bleiben die bereits vorhandenen Termine absichtlich in der Datenbank erhalten.

Dadurch bleiben vergangene und erledigte Termine weiterhin in der Historie nachvollziehbar.

Da der zugehörige Auftrag nicht mehr existiert, können diese Termine anschließend nicht mehr bearbeitet werden.

### Integriertes Chat-System

Nach der Zuordnung können Helfer und pflegebedürftige Person direkt miteinander kommunizieren.

Der Helfer muss die pflegebedürftige Person zuerst kontaktieren.

Die pflegebedürftige Person kann den Chat daher nicht selbstständig beginnen.

Sobald der Helfer die erste Nachricht gesendet hat, kann die pflegebedürftige Person auf die Nachricht antworten.

Der Chat bietet:

- datenbankgestützte Nachrichten,
- eine Darstellung im WhatsApp-Stil,
- eine unterschiedliche Ausrichtung für eigene und empfangene Nachrichten,
- eine Soft-Delete-Funktion zum Leeren des eigenen Chatverlaufs.

Ein neuer Chat ist nur möglich, wenn zwischen den beiden Nutzern ein gemeinsamer angenommener Auftrag besteht.

Wird ein Auftrag gelöscht, bleiben die bereits geschriebenen Nachrichten absichtlich in der Datenbank erhalten.

Der bisherige Chatverlauf kann weiterhin angezeigt werden.

Da kein gemeinsamer Auftrag mehr existiert, können anschließend keine neuen Nachrichten mehr gesendet werden.

### Profilverwaltung

Nutzer können ihre persönlichen Daten bearbeiten.

Helfer können zusätzlich ihren Vorstellungstext aktualisieren.

Der Vorstellungstext wird pflegebedürftigen Personen bei einer Bewerbung angezeigt.

E-Mail-Adresse und Telefonnummer werden auf bereits vorhandene Einträge geprüft, damit keine doppelten Werte gespeichert werden.

Texteingaben werden vor der Verarbeitung von überflüssigen Leerzeichen bereinigt.

Passwörter bleiben von dieser Bereinigung ausgenommen.

### Sichere Authentifizierung

Die Anwendung verwendet:

- gehashte Passwörter mit Werkzeug,
- Session-Management mit Flask-Login,
- `@login_required` für geschützte Routen,
- rollenbasierte Zugriffskontrollen,
- CSRF-Schutz über Flask-WTF.

## Verwendete Technologien

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Bootstrap 5
- SQLite
- Jinja2
- Werkzeug

## Installation

### 1. Repository klonen

```bash
git clone <REPOSITORY-URL>
cd Projekt_Team14
```

### 2. Virtuelle Umgebung erstellen

```bash
python -m venv venv
```

### 3. Abhängigkeiten installieren

```bash
python -m pip install -r requirements.txt
```

### 4. Anwendung starten

```bash
python app.py
```

Die Anwendung ist anschließend normalerweise unter folgender Adresse erreichbar:

```text
http://127.0.0.1:5000
```

## Happy Path

### Variante mit eigener Registrierung

1. Anwendung starten.
2. Als pflegebedürftige Person registrieren.
3. Als Admin anmelden.
4. Den neu registrierten Nutzer in der Nutzerübersicht freigeben.
5. Als pflegebedürftige Person anmelden.
6. Einen Auftrag erstellen und veröffentlichen.
7. Ausloggen.
8. Als Helfer registrieren.
9. Einen Vorstellungstext eingeben.
10. Ein Führungszeugnis als PDF hochladen.
11. Als Admin anmelden.
12. Das Führungszeugnis prüfen.
13. Den Helfer freigeben.
14. Als Helfer anmelden.
15. Die offenen Aufträge öffnen.
16. Auf den Auftrag der pflegebedürftigen Person bewerben.
17. Ausloggen.
18. Als pflegebedürftige Person anmelden.
19. Die eingegangenen Bewerbungen öffnen.
20. Die Bewerbung des Helfers annehmen.
21. Ausloggen.
22. Als Helfer anmelden.
23. Den Chat mit der pflegebedürftigen Person öffnen.
24. Als Helfer die erste Testnachricht senden.
25. Ausloggen.
26. Als pflegebedürftige Person anmelden.
27. Den vorhandenen Chat öffnen.
28. Auf die Nachricht des Helfers antworten.
29. In der Terminübersicht einen Termin anfragen.
30. Ausloggen.
31. Als Helfer anmelden.
32. Den vorgeschlagenen Termin bestätigen oder ablehnen.
33. Weitere Termine anfragen.
34. Termine bearbeiten oder löschen.
35. Einen Termin als erledigt markieren.
36. Den abgeschlossenen Termin über die Historie erneut ansehen.

## Verhalten beim Löschen eines Auftrags

Beim Löschen eines Auftrags wird der Auftrag vollständig aus der Datenbank entfernt.

Die bereits vorhandenen Termine und Nachrichten werden jedoch absichtlich nicht mitgelöscht.

Für die gespeicherten Termine gilt anschließend:

- Die Termine bleiben in der Datenbank erhalten.
- Erledigte Termine bleiben in der Historie sichtbar.
- Der zugehörige Auftrag ist nicht mehr vorhanden.
- Die Termine können nicht mehr bearbeitet werden.

Für die gespeicherten Nachrichten gilt anschließend:

- Die Nachrichten bleiben in der Datenbank erhalten.
- Der bisherige Chatverlauf bleibt sichtbar.
- Es können keine neuen Nachrichten mehr gesendet werden.
- Ein neuer Chat ohne bestehenden Auftrag kann nicht begonnen werden.

Dieses Verhalten dient dazu, vergangene Kommunikation und bereits durchgeführte Termine weiterhin nachvollziehen zu können.

## Vorhandene Testnutzer

Für Entwicklungs- und Demonstrationszwecke werden beim Start Testnutzer angelegt, sofern sie noch nicht existieren.

| Rolle | E-Mail-Adresse | Passwort |
|---|---|---|
| Admin | `admin@email.com` | `12345678` |
| Helfer | `helfer1@email.com` | `12345678` |
| Helfer | `helfer2@email.com` | `12345678` |
| PP | `pp1@email.com` | `12345678` |
| PP | `pp2@email.com` | `12345678` |

Die Testnutzer sind bereits freigegeben.

## Hinweise

- Hochgeladene Führungszeugnisse werden im aktuellen Prototyp ausschließlich zu Demonstrationszwecken verwendet.
- Der Helfer muss nach der Annahme einer Bewerbung den ersten Kontakt im Chat herstellen.
- Termine und Nachrichten werden beim Löschen eines Auftrags absichtlich nicht gelöscht.
- Termine ohne zugehörigen Auftrag können nicht mehr bearbeitet werden.
- In einem Chat ohne zugehörigen Auftrag können keine neuen Nachrichten mehr gesendet werden.

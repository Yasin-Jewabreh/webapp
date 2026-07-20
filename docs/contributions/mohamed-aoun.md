---
title: Mohamed Aoun 
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Mohamed Aoun

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade
Ich möchte in diesem Kurs eine 1,0 erreichen.

### Personal goals
Ich möchte in diesem Kurs die Grundlagen von Python und der Webentwicklung erlernen. Konkret möchte ich verstehen, wie Flask, SQLAlchemy und Jinja2-Templates zusammenarbeiten. Außerdem möchte ich lernen, wie man im Team professionell mit Git und GitHub arbeitet, Branches erstellt, Merge-Konflikte löst und Pull Requests durchführt.

---

## Eidesstattliche Erklärung

**[Mohamed Aoun, Matrikelnr.: 77205967095]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierter Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Entwicklung der Chat-Funktionalität mit Partner-Liste und WhatsApp-Stil | Der Chat ermöglicht eine flüssige Kommunikation zwischen Helfer und PP. Nachrichten werden dynamisch links und rechts angezeigt, je nach Absender. | Während der Entwicklung nutzte die Chat-Route bewusst eine Platzhalter-ID (`sender_id=1`), da das Login-System zu diesem Zeitpunkt noch nicht fertiggestellt war und `current_user` nicht verfügbar war. Nach Integration von Flask-Login habe ich die Route vollständig auf `current_user.id` umgestellt und die Nachrichtenfilterung auf echte Nutzerpaare erweitert. |
| 2 | Erstellung der `base.html` mit Bootstrap Pulse Theme | Die `base.html` bildet das robuste, gemeinsame Grundgerüst für alle Seiten. Das Pulse Theme sorgt für ein professionelles und einheitliches UI-Design. | Ich musste die Jinja2-Template-Vererbung (`extends`/`block`) auf unser konkretes Projekt anwenden und Bootstrap datenschutzkonform über Flask-Bootstrap einbinden, anstatt die Google Fonts API zu nutzen. |
| 3 | Implementierung der automatischen Zeitzonen-Erfassung (Berlin) | Nachrichten werden mit der korrekten deutschen Uhrzeit angezeigt, wobei automatisch zwischen Sommer- und Winterzeit unterschieden wird. | Ich musste erkennen, dass SQLite Zeitstempel standardmäßig in UTC speichert und beim Anzeigen im Frontend nicht automatisch konvertiert. Die Lösung erforderte das Verständnis und die Einbindung des `pytz`-Moduls. |

## Design Decisions that I led

1. [DD-04: Gemeinsames Grundgerüst mit base.html und Bootstrap](../design-decisions/dd-04.md)
2. [DD-05: Chat-Route und Nachrichtenstruktur](../design-decisions/dd-05.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Erstellung der base.html mit Bootstrap Pulse Theme | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/5ae8579) | [Bootstrap Docs](https://getbootstrap.com/docs/5.3/), [Bootstrap-Flask Docs](https://bootstrap-flask.readthedocs.io/), [Kurs-Tutorial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html) |
| Entwicklung der Chat-Route mit Partner-Liste und Umstellung auf `current_user` | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/a3a1fb9) | [Flask Docs](https://flask.palletsprojects.com/), [SQLAlchemy Docs](https://docs.sqlalchemy.org/), [Flask-Login Docs](https://flask-login.readthedocs.io/) |
| Redesign des Chat-Templates im WhatsApp-Stil | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/1a0fae4) | [Bootstrap Docs](https://getbootstrap.com/docs/5.3/) |
| Implementierung der Berlin-Zeitzone mit pytz | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/30c63ca) | [pytz Docs](https://pythonhosted.org/pytz/) |
| Dokumentation DD-04 und DD-05 | [DD-04](../design-decisions/dd-04.md), [DD-05](../design-decisions/dd-05.md) | Eigene Architektur-Entscheidungen |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | Claude (claude.ai) | Erklärung spezifischer Bootstrap-Klassen für das Chat-Layout (z.B. `d-flex`, `justify-content-end`, `ms-auto`) die nicht im Kurs-Tutorial abgedeckt waren | `chat.html` | Die grundlegende Bootstrap-Einbindung folgte dem Tutorial. KI wurde ergänzend genutzt, um das WhatsApp-spezifische Layout (Nachrichten links/rechts) zu verstehen. Implementierung erfolgte eigenständig. |
| 02 | Claude (claude.ai) | Konzeptionelle Unterstützung beim Design der `Nachricht`-Klasse in SQLAlchemy mit zwei Foreign Keys auf dieselbe Tabelle (Sender und Empfänger) | `models.py` | Das SQLAlchemy-Tutorial deckte einfache Relationships ab. Die Besonderheit zweier `db.relationship()`-Einträge mit `foreign_keys`-Parameter für dasselbe Modell wurde mit KI-Hilfe verstanden und eigenständig implementiert. |
| 03 | ChatGPT | Brainstorming zu Architektur-Entscheidungen für das gemeinsame Template (Struktur der `base.html`) | `base.html`, DD-04 | Diskussion von Best-Practices als Ergänzung zum Tutorial. Die finale Entscheidung und Ausformulierung der DD-04 erfolgten eigenständig. |
| 04 | Gemini | Problemanalyse: UTC-Zeitstempel werden in SQLite ohne Zeitzoneninfo gespeichert und im Frontend falsch dargestellt | `models.py` | Das Problem wurde durch Testen im Browser entdeckt (Uhrzeit stimmte nicht). Gemini half beim Verständnis des Unterschieds zwischen UTC und Lokalzeit. Die Einbindung von `pytz` in die `berlin_time()`-Funktion habe ich eigenständig umgesetzt. |

---

## Reflection

Zu Beginn des Projekts waren HTML, CSS und das Konzept eines Web-Frameworks für mich vollständiges Neuland. Durch die Entwicklung der `base.html` habe ich zunächst verstanden, wie Jinja2-Template-Vererbung funktioniert und wie Bootstrap als CSS-Framework das Styling systematisiert. Das Kurs-Tutorial war dabei die primäre Grundlage – KI nutzte ich ergänzend, um projektspezifische Fragen zu klären, die im Tutorial nicht abgedeckt waren.

Die größte technische Herausforderung war die Chat-Funktionalität. Da das Login-System zu Beginn noch nicht fertiggestellt war und `current_user` daher nicht zur Verfügung stand, verwendete die Chat-Route bewusst eine Platzhalter-ID (`sender_id=1`), um die grundlegende Funktionalität früh testen zu können. Sobald Flask-Login integriert war, habe ich die Route vollständig überarbeitet: `sender_id=1` wurde durch `current_user.id` ersetzt und die Nachrichtenabfrage so angepasst, dass nur noch Nachrichten zwischen zwei konkreten Nutzern angezeigt werden. Das erforderte ein tiefes Verständnis davon, wie Flask-Login, SQLAlchemy-Abfragen und der aktive Session-Kontext zusammenspielen. Zusätzlich entdeckte ich beim Testen, dass alle Zeitstempel in UTC gespeichert wurden und die angezeigte Uhrzeit dadurch um eine bis zwei Stunden abwich. Die Lösung über das `pytz`-Modul mit der `berlin_time()`-Funktion habe ich nach Verständnis des Problems eigenständig implementiert.

Eine weitere Herausforderung war die Teamarbeit über Git. Mein `feature/chat`-Branch lief parallel zu vielen anderen Änderungen im Team, was zu Merge-Konflikten führte. Ich habe dabei gelernt, wie wichtig es ist, Branches regelmäßig zu synchronisieren und Änderungen frühzeitig in den Hauptbranch zu mergen, um spätere Konflikte zu minimieren.

Für zukünftige Projekte möchte ich von Anfang an konsequenter auf sauberes Branch-Management achten und früher Pull Requests stellen, statt lange auf einem isolierten Branch zu arbeiten. Inhaltlich möchte ich meine Kenntnisse in fortgeschrittener Datenbankmodellierung und sicherem Session-Management vertiefen.
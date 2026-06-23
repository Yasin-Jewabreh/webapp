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
| 1 | Entwicklung der Chat-Funktionalität mit Partner-Liste und WhatsApp-Stil | Der Chat ermöglicht eine flüssige Kommunikation zwischen Helfer und PP. Nachrichten werden dynamisch links und rechts angezeigt, je nach Absender. | Ich musste Flask-Routen, SQLAlchemy-Abfragen und Jinja2-Templates nahtlos kombinieren und diverse Merge-Konflikte lösen. |
| 2 | Erstellung der `base.html` mit Bootstrap Pulse Theme | Die `base.html` bildet das robuste, gemeinsame Grundgerüst für alle Seiten. Das Pulse Theme sorgt für ein professionelles und einheitliches UI-Design. | Ich musste das Konzept der Jinja2-Template-Vererbung (`extends`/`block`) verstehen und Bootstrap datenschutzkonform einbinden. |
| 3 | Implementierung der automatischen Zeitzonen-Erfassung (Berlin) | Nachrichten werden mit der korrekten deutschen Uhrzeit angezeigt, wobei automatisch zwischen Sommer- und Winterzeit unterschieden wird. | Ich musste die Limitationen von Standard-UTC-Zeitstempeln verstehen und erlernen, wie das Modul `pytz` diese lokal korrekt verarbeitet. |

## Design Decisions that I led

1. [DD-04: Gemeinsames Grundgerüst mit base.html und Bootstrap](../design-decisions/dd-04.md)
2. [DD-05: Chat-Route und Nachrichtenstruktur](../design-decisions/dd-05.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Erstellung der base.html mit Bootstrap Pulse Theme | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/5ae8579) | [Bootstrap Docs](https://getbootstrap.com/docs/5.3/), [Flask-Bootstrap Docs](https://bootstrap-flask.readthedocs.io/) |
| Entwicklung der Chat-Route mit Partner-Liste | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/a3a1fb9) | [Flask Docs](https://flask.palletsprojects.com/), [SQLAlchemy Docs](https://docs.sqlalchemy.org/) |
| Redesign des Chat-Templates im WhatsApp-Stil | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/1a0fae4) | [Bootstrap Docs](https://getbootstrap.com/docs/5.3/) |
| Implementierung der Berlin-Zeitzone mit pytz | [Commit](https://github.com/Yasin-Jewabreh/webapp/commit/30c63ca) | [pytz Docs](https://pythonhosted.org/pytz/) |
| Dokumentation DD-04 und DD-05 | [DD-04](../design-decisions/dd-04.md), [DD-05](../design-decisions/dd-05.md) | Eigene Architektur-Entscheidungen |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | Claude (claude.ai) | Erklärung der HTML-Grundstruktur und CSS-Konzepten wie margin, padding und Bootstrap-Klassen | `base.html`, `chat.html` | Konzepte wurden als interaktiver Lern-Tutor genutzt. Die eigentliche Implementierung und Anpassung auf unser Projekt erfolgte eigenständig. |
| 02 | Claude (claude.ai) | Erklärung von Jinja2-Template-Vererbung und dem Flask-Routing-Prinzip | `app.py`, `chat.html`, `base.html` | Theoretische Grundlagen wurden erfragt. Der finale Routing-Code wurde selbst geschrieben und iterativ im Browser getestet. |
| 03 | Claude (claude.ai) | Konzeptionelle Unterstützung beim Design der Nachrichten-Klasse in SQLAlchemy | `models.py` | Das relationale Konzept (Foreign Keys für Sender/Empfänger) wurde verifiziert. Die Model-Klasse wurde eigenständig strukturiert. |
| 04 | Claude (claude.ai) | Hilfestellung beim Verständnis des Git-Workflows (Branches, Merge-Konflikte) | Git-Workflow | Befehle wurden zur Vermeidung von Datenverlust vorab abgefragt und anschließend manuell im Terminal ausgeführt. |
| 05 | ChatGPT | Brainstorming zu Architektur-Entscheidungen für das gemeinsame Template | `base.html`, DD-04 | Diskussion von Best-Practices. Die finale Entscheidung und die Ausformulierung der DD-04 erfolgten durch mich. |
| 06 | Gemini | Problemanalyse bezüglich fehlerhafter UTC-Zeitstempel in der lokalen Anzeige | `models.py` | Das Problem wurde identifiziert und Lösungsansätze diskutiert. Die Einbindung von `pytz` in die Model-Instanziierung habe ich eigenständig programmiert. |

---

## Reflection

Im Verlauf des Projekts habe ich die grundlegende Architektur der Full-Stack-Webentwicklung kennengelernt. Zu Beginn waren HTML und CSS für mich komplett neu. Durch die schrittweise Entwicklung der `base.html` und des komplexen Chat-Templates habe ich praxisnah gelernt, wie Frontend (Jinja2) und Backend (Flask/Python) dynamisch zusammenarbeiten.

Eine große Herausforderung war die Organisation über Git und GitHub, insbesondere das Navigieren durch Branches und das Lösen von Merge-Konflikten. Ich habe gelernt, dass saubere, isolierte Commits die Zusammenarbeit im Team essenziell erleichtern und Fehler minimieren.

Die Chat-Funktionalität war mein technisch anspruchsvollster Beitrag. Ich musste evaluieren, wie dynamische Flask-Routen, gefilterte SQLAlchemy-Abfragen und Jinja2-Bedingungen (If-Statements für Sender und Empfänger) ineinandergreifen müssen, um einen funktionalen Chat mit korrekter Nachrichtenanzeige aufzubauen.

Für zukünftige Projekte möchte ich meine Python-Kenntnisse noch weiter vertiefen und insbesondere mehr Erfahrung im Bereich fortgeschrittener Datenbankmodellierung und sicherem Session-Management (Login-Systeme) sammeln.
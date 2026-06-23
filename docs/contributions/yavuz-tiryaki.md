---
title: Yavuz Tiryaki
parent: Individual Contributions
nav_order: 1
---


{: .no_toc }
# Yavuz Tiryaki

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

Meine Zielnote ist die 1,0 hierfür werde ich mein bestes geben

### Personal goals

Primär will ich mir aus dem Kurs den Umgang mit python beibringen. Denn ich bin mir sicher das, dass nicht das letzte Mal sein wird das ich python nutzen muss. 
Außerdem ist es auch das erstemal das ich github nutzen muss weswegen es mir auch wichtig ist die Bedinung dessen zu erlernen. Sowie auch die Theoretischen Punkte der Website Development zu verstehen und einsetzen zu können

---

## Eidesstattliche Erklärung

**[Yavuz Selim Tiryaki 77209615722]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Entwicklung des Auftragbereichs für Helfer| Der Helfer Auftragsübersicht ist ein wichtiger Teil für die Benutzerfreundlichekit und auch die allgemeine Übersicht für den Helfer um zu erkennen welche die noch Offenen Aufträge, eine Auftrag annehmen und angenommenen Aufträge verwalten.| Ich musste mich erst allgemein mit der Struktur bekannt machen. Zum Beispiel dem Routing (Flask-Route), Datenbankmodell Sqlite mit der ausführung von SQLAlchemy, die Spaltung der Rollen über die nutzer.id die wir mit einer db.relationship erstellt haben und auch HTML&BootStrap5 für das allgemeine Design um es den Nutzern Veranschaulichen|
| 2 | Entwicklung der Auftrag erstellung | Diese musste mit dem login impementiert werden so das man weiß das es der Nutzer ist der nach einer Hilfe sucht. Das wurde bei der Registrierung vom Nutzer ausgewählt und in der Datenbank auch danach abgespeichert. Außerdem durch die Implementierung des Logins habe ich es durch das @login_required hingekriegt die eingespeicherten Login Daten bei der Erstellung zu übernehmen so das der Nutzer es nicht mehr selber noch einmal einzugeben | Vorallem war die einteilung der Rollen eine schwierige Challange die wir mit Salih gemeinsam ausprobiert haben. Außerdem auch natürlich die ganze überprüfung das es denn auch wirklich der Hilfe suchende und hilfe anbietende|
| 3 | Die Ausarbeitung für die Product-Discovery | Ich hab an den Aufgaben product-discovery unsere essenziellen Probleme der Zielgruppen zu erkennen so wie auch die echte Meinung von Auszubildenden und Studenten der HWR sowie auch anderen Instituten. Dadurch konnten wir unsere Ziele fürs Projekt nochmal besser definieren und dokumentieren | Ich musste mir einige Quellen durchlesen damit wir die genaueun Probleme dieser beiden Zielgruppen haben damit danach die Kriterien der webapp bestimmt werden konnte |

## Design Decisions that I led

1. [DD #01](docs/design-decisions/dd-01.md)
2. [DD #06](docs/design-decisions/dd-06.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Auftrag erstellen | [Commit 4be7955 | 
](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [Commit 09f7c0b](https://github.com/Yasin-Jewabreh/webapp/commit/09f7c0bc59a9315834bfc4bb3cd1901d20f5a577), [Commit 4be7955] | (https://github.com/hwrberlin/fswd/commit/75a6c1) | 
[Commit fe627b7
](https://github.com/Yasin-Jewabreh/webapp/commit/fe627b7ee028b674391f261b6c6a8c6d8c02b437s) |


---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |    ChatGPT     |     Rechechen und Ideenfindung           |          Product Discovery                        |                             |
| 02  |      Gemini   |        Debugging of the Code        |                               |                             |
| 03 |     ChatGPT    |       Git-Befehle und Unterstützung bei Git-Konflikten (Pull and Push Request)  |                                 |                             |
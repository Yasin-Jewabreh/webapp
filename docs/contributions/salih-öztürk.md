---
title: Salih Öztürk
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Salih Öztürk

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

Ich strebe in diesem Modul eine gute bis sehr gute Note (1,7 – 1,3) an.

### Personal goals

Mein Ziel ist es, meine Fähigkeiten im Bereich Fullstack Web Development zu verbessern.  
Ich möchte insbesondere den Umgang mit GitHub, Teamarbeit in Softwareprojekten sowie Backend- und Frontend-Integration besser verstehen.

---

## Eidesstattliche Erklärung

**[Salih Öztürk, Matrikelnr.: 77204798325 ]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Entwicklung der Registrierungs- und Login-Funktion mit Flask, SQLAlchemy und Flask-Login  | Die Benutzeranmeldung ist eine zentrale Funktion der Plattform und bildet die Grundlage für viele weitere Features | Das Verständnis von Benutzerauthentifizierung sowie die Anbindung von Formularen an die Datenbank |
| 2 | Erstellung des Dashboards und der Profilseite für angemeldete Nutzer | Nutzer können dadurch ihre persönlichen Informationen einsehen und die Plattform komfortabel nutzen | Die Verknüpfung von Backend-Daten mit den HTML-Templates und Benutzersitzungen |
| 3 | Entwicklung der Startseite sowie der grundlegenden Navigation | Die Startseite vermittelt den ersten Eindruck der Plattform und verbessert die Benutzerfreundlichkeit | Die Abstimmung des Designs mit den bereits vorhandenen Teambeiträgen und die Integration in die bestehende Struktur |

---

## Design Decisions that I led

1. [DD #02] Erforderliche Benutzerinformationen bei der Registrierung
2. [DD #03] Strategie zur Benutzerverifizierung

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Implementierung der Benutzerregistrierung | Git-Commits zur Registrierung und Datenbankanbindung | Flask-Dokumentation, SQLAlchemy-Dokumentation, ChatGPT |
| Implementierung der Benutzerregistrierung | Create login and registration templates, Add login and register routes, Add login and register routes with GET and POST support | Flask-Dokumentation, SQLAlchemy-Dokumentation, ChatGPT |
| Implementierung der Login-Funktion | Configure Flask-Login user loader, Add UserMixin to Nutzer model, Add logout route using Flask-Login, Improve login validation feedback | Flask-Login-Dokumentation, ChatGPT |
| Entwicklung des Dashboards | add dashboard, Add back button navigation, redirect accepted order confirmation back to dashboard | Flask-Dokumentation, Teamdiskussionen, ChatGPT |
| Entwicklung der Profilseite | Add profile page, modernize profile view with Bootstrap card layout and WTForms macro | Flask-Dokumentation, Teamdiskussionen, ChatGPT |
| Entwicklung der Startseite | Add landing page template, Connect start page template to route, Fix start page template | Teamdiskussionen, ChatGPT |
| Erstellung der Design Decisions DD-02 und DD-03 | Design Decision required Information of the user, Create DD-03 and update DD-02 record, Revise DD-03 and defer user verification | Teamdiskussionen |
| Zusammenarbeit über GitHub (Branches, Commits und Merges) | Merge main into feature/login, Merge remote-tracking branch origin/main into feature/dashboard, Merge pull request #5 from feature/login | GitHub-Dokumentation |
---

## AI Directory

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks |
| :-- | :--     | :--            | :--                             | :--     |
| 01 | ChatGPT | Unterstützung beim Verständnis von Flask, SQLAlchemy, Git und bei der Erstellung von Dokumentation | Login, Registrierung, Dashboard, Profilseite, DD-02, DD-03, Contributions-Datei | Inhalte wurden überprüft, angepasst und eigenständig umgesetzt |
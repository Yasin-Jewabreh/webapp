---
title: Yasin Jewabreh
parent: Individual Contributions
nav_order: 1
---
{: .no_toc }
# Yasin Jewabreh

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

Ich strebe eine 1.0 an und werde das nötige dafür tun.

### Personal goals

Ich habe mehrere Ziele in Bezug auf diesen Kurs:
1. Ich möchte lernen, mit Python umzugehen und es möglichst ohne Hilfe nutzen zu können
2. Ich möchte git und github unabhänig nutzen und verstehen kann, ohne ständing ins Tutorial gucken zu müssen
3. Ich möchte eine simple Webapp alleine codieren können

---

## Eidesstattliche Erklärung

**[Yasin Jewabreh, Matrikelnr.: 77204640258]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

`Das Folgende wird im weiteren Verlauf des Projektes ausgefüllt!`
---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Ich habe mich um die Terminübersicht gekümmert. Dazu gehören viele Funktionen: Termine erstellen, bearbeiten, löschen, annehmen, ablehnen und auf erledigt setzen. Ich lasse die vereinbarten Termine, die Termine, die bestätigt werden müssen, die Termine, bei denen man auf eine Antwort wartet, und die Terminhistorie anzeigen.  | Ich bin ziemlich stolz, weil ich Schritt für Schritt die einzelnen Funktionen hinzugefügt habe. Und auch wenn ich Probleme hatte, habe ich das Log durchsucht. Mittlerweile verstehe ich wie man ein Problem findet, ich muss auch sagen, dass ich mich mittlerweile sehr gut mit Git und Vscode auskenne. Ich habe meine Ziele erreich | Die Probleme die ich überwunden habe, sind, dass ich mit den Problemmessages im Terminal nicht klar kam. Ich konnte die Fehler anfangs nicht finden und habe viel Zeit verloren. Außerdem habe ich den Umgang mit Branches erst spät verstanden. |
| 2 | Meine Größte Contribution war jede Funktion in Bezug auf die Termine. Allerdings habe ich auch Design Decisions geleitet, wie den Umgang mit SQLAlchemy  |  |  |
| 3 |  |  |  |

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md)
2. [DD #01](../design-decisions/dd-01.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [Commit 1](https://github.com/hwrberlin/fswd/commit/d816e4), [Commit 2](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
|  |  |  |
|  |  |  |
|  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |    GEMINI     |   Bootstrap class Design             |       termine.html                          |  Ich bin so vorgegangen, dass ich mir Zwischenziele gesetzt habe und erstmal versucht habe, es selbst hinzubekommen mit dem Layout. Wenn ich nicht weiterwusste, habe ich GEMINI gefragt und er hat mir z.B. gesagt, wie ich einen Tabelleninhalt anklickbar mache,nachdm es bei mir nicht geklappt hatte mit meinem Code.                          |
| 02  |      GEMINI   |        Anzeigen von Flash Messages        |       base.html                          |         Das ist die enzige Sache die ich einfach von der KI reinkopiert habe, sonst habe ich alles selbst geschrieben.                    |
| 03 |     GEMINI    |        Fehlermessages erklären        |         app.py                        |        Ich hatte Fehlercodes, als ich eine Liste mit .scalars() (wie im Tutorial) angelegt habe. Gemini  hat mir dann gesagt, dass ich ein .all() einfügen kann damit es klappt. Danach hat es geklappt .                  |

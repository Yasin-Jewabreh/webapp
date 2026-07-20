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
| 2 |  Ich habe am Ende übernommen, die einzelnen Code Teile zusammenzuführen und die Probleme zu beheben. Dazu gehörte vor Allem Fehler, wie z.B. falsche Weiterleitungen etc., aber auch Unstimmigkeiten in der Datenbanklogik mit dem Code.  | Ich bin auch hier stolz, weil ich gemerkt habe, dass ich den gesamten Code gut verstanden habe. Ich wusste fast immer direkt wo ich den Fehler suchen muss und wusste dann auch, wie ich ihn beheben kann | Aufgrund von wahrscheinlich interner Fehlkommunikation gab es in der Klassenstruktur kleine Abweichungen, die ich dementsprechend ausgebessert habe. Das Refactoring hat hier sehr geholfen|
| 3 | Zu der Termin erstellen Funktion gehört natürlich auch ein Formular mit WTForms. Hier habe ich das Formular und zusätzlich auch Validierungsfunktionen erstellt, um die Fehleranfälligkeit bei falschen Eingaben zu reduzieren und den Programmfluss sicher zu stellen  | Das schwierige war manchmal die genaue Syntax besonders von den Funktionen, hier hat ein Blick in die Dokumentation von WTForms aber auch sehr geholfen. |

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md)
2. [DD #07](../design-decisions/dd-07.md)

---

## Contributions
Alles auf dem Branch calendar.html gehört zu meinen Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Termin Formulare mit WTForms|  Z.B. Commit: (bc9824f8acf94abf63bde9c1bb4689610a50e56b) | Tutorial von Herrn Eck, [WTF Dokumentation](https://wtforms.readthedocs.io/en/3.2.x/) |
| Rollenbasierte Termin-Statussegmentierung | Commit1(65ff339d3414bd5a976e587e09babb7a9d6ed72e),Commit2(0d8f30fab0832825208461454640e7c67b5e7358), Commit3(72f6508b95ef624b5f1f96183bb26bbe8ed0735b) (alles im o.g. Branch) | Tutorial von Herrn Eck für die SQLAlchemy Syntax etc. |
| JSON API für die Termine | Commit(e55594214f404c1b33ff22460dc8c5ebfb1aa74a) | Tutorial von Herrn Eck, Gemini (siehe AIDirectory Eintrag 04)|
| CRUD für Termine | Commit1(21a0c39bb00389706b651ef8e50ad5c44a506ed5), siehe oben für die forms | Tutorial Herr Eck, Gemini (siehe AI Directory Eintrag 03) |
| Zusammenführen des Codes   | Z.B. Commit(49c9ae3576481af94317d68e0e0fe44e94699658), Commit(abf1c08fc4af9adb49aae6969eb2eaf5bc5992f3) | Tutorial Herr Eck |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |    GEMINI     |   Bootstrap class Design             |       termine.html                          |  Ich bin so vorgegangen, dass ich mir Zwischenziele gesetzt habe und erstmal versucht habe, es selbst hinzubekommen mit dem Layout. Wenn ich nicht weiterwusste, habe ich GEMINI gefragt und er hat mir z.B. gesagt, wie ich einen Tabelleninhalt anklickbar mache, nachdem es bei mir nicht geklappt hatte, den Text Zeile einfach als Link zu machen.                         |
| 02  |      GEMINI   |        Anzeigen von Flash Messages        |       base.html                          |         Das ist die einzige Sache, die ich einfach von der KI reinkopiert habe, sonst habe ich alles selbst geschrieben.                    |
| 03 |     GEMINI    |        Fehlermessages erklären        |         app.py                        |        Ich hatte Fehlercodes, als ich eine Liste mit .scalars() (wie im Tutorial) angelegt habe. Gemini  hat mir dann gesagt, dass ich ein .all() einfügen kann damit es klappt. Danach hat es geklappt .                  |
| 04 | GEMINI | Probleme mit der JSON Headless API lösen | app.py | Mit dem Code aus dem Tutorial allein, kamen nur Fehlercodes und ich habe es allein nicht geschafft, es zum laufen zu kriegen. Gemini hat mir z.B. dabei geholfen, dass ich die Date- Variablen in einen String umwandeln muss.


Nachtrag zu Eintrag 1 des AI Directories: Die Funktion, den Tabelleninhalt anzuklicken, um den Termin zu bearbeiten, wurde entfernt. Da der Vorschlag von GEMINI KI enthielt. 

Nachtrag zu Eintrag 2 des AI Directories: Diese Funktion wurde entfernt und stattdessen das Bootstrap design aus dem Tutorial gewählt. Welches am Anfang übersehen wurde. Demzufolge gibt es hier keine KI Nutzung und kein JavaScript mehr.
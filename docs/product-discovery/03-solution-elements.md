---
title: Solution Elements
parent: Product Discovery
nav_order: 3
---

{: .no_toc }
# Solution Elements

## Raw Material

Nachdem wir uns mit den Problemen unserer beiden Zielgruppen beschäftigt hatten, haben wir überlegt, wie sich diese miteinander verbinden lassen. Auf der einen Seite gibt es Menschen, die bei bestimmten Aufgaben im Alltag Unterstützung benötigen. Auf der anderen Seite suchen viele Studierende/Auszubildende nach einer Möglichkeit, neben dem Studiu/Ausbildung flexibel Geld zu verdienen.

Daraus entstand die Idee für **HelpYourNeighbour**. Die Webanwendung soll hilfesuchende Personen und Helfer aus ihrer Umgebung zusammenbringen. Dabei geht es nicht um professionelle Pflege, sondern um kleinere Aufgaben, für die keine pflegerische oder medizinische Ausbildung notwendig ist.

Dass Unterstützung im Alltag einen großen Stellenwert hat, zeigt eine Untersuchung des Deutschen Zentrums für Altersfragen. Im Jahr 2023 unterstützten, betreuten oder pflegten rund 23 Prozent der Menschen zwischen 43 und 65 Jahren regelmäßig eine andere Person. Rund 4,2 Millionen Menschen dieser Altersgruppe übernahmen dabei ausschließlich Aufgaben wie Hilfe im Haushalt, Betreuung oder Begleitung.[1]

Auch das Zentrum für Qualität in der Pflege beschreibt Angehörige als eine wichtige Grundlage der häuslichen Versorgung. Gleichzeitig kann die regelmäßige Unterstützung für die beteiligten Personen zu einer Belastung werden.[2] Unsere Anwendung soll Angehörige nicht ersetzen, könnte aber bei einzelnen Aufgaben im Alltag zusätzliche Unterstützung vermitteln.

Bei den Studierenden zeigt sich ebenfalls ein Bedarf. Laut der 22. Sozialerhebung gehen 63 Prozent der Studierenden neben ihrem Studium einer Erwerbstätigkeit nach. Durchschnittlich arbeiten sie etwa 15 Stunden pro Woche. Gleichzeitig benötigen sie ungefähr 34 Stunden pro Woche für Lehrveranstaltungen und Selbststudium.[3] Deshalb war uns wichtig, keine festen Arbeitszeiten vorzugeben. Die Helfer sollen selbst entscheiden können, ob und wann sie einen Auftrag übernehmen.

## Grundidee

Eine hilfesuchende Person erstellt einen Auftrag und beschreibt darin, wobei sie Unterstützung benötigt. Denkbar sind zum Beispiel:

- Einkaufen,
- Unterstützung im Haushalt,
- Möbel aufbauen,
- technische Geräte einrichten,
- Begleitung bei Erledigungen,
- kleinere organisatorische Aufgaben.

Registrierte Helfer können die offenen Aufträge ansehen. Passt ein Auftrag zeitlich und inhaltlich, kann er angenommen werden. Die genaueren Einzelheiten werden danach über die Nachrichtenfunktion geklärt.

Unser Ziel ist kein klassischer Nebenjob mit festen Schichten. Stattdessen sollen einzelne Aufträge vermittelt werden, die Helfer passend zu ihrem Stundenplan auswählen können.

## Erste Überlegungen

Zu Beginn hatten wir überlegt, alle Informationen direkt in der Auftragsübersicht anzuzeigen. Dazu hätten auch der vollständige Name, die Adresse, die genaue Uhrzeit und weitere persönliche Angaben gehört.

Diese Idee haben wir verworfen. In unserer eigenen Umfrage wurde mehrfach der Wunsch nach Sicherheit und einem vorsichtigen Umgang mit persönlichen Daten genannt.[4] Außerdem ist es für eine erste Entscheidung nicht notwendig, sofort die vollständige Adresse einer hilfesuchenden Person zu sehen.

Die Auftragsübersicht soll daher zunächst nur die wichtigsten Informationen enthalten. Genauere Angaben werden erst später zwischen den beteiligten Personen ausgetauscht.

## Benutzerrollen

Für HelpYourNeighbour sind zwei unterschiedliche Rollen vorgesehen.

### Hilfesuchende Person

Eine hilfesuchende Person kann:

- ein Benutzerkonto erstellen,
- einen Auftrag einstellen,
- die benötigte Hilfe beschreiben,
- den Status des eigenen Auftrags ansehen,
- mit einem Helfer Nachrichten austauschen,
- einen Termin vereinbaren.

### Helfer

Ein Helfer kann:

- ein Benutzerkonto erstellen,
- offene Aufträge ansehen,
- einen Auftrag auswählen und annehmen,
- die eigenen angenommenen Aufträge verwalten,
- mit der hilfesuchenden Person schreiben,
- einen vereinbarten Termin ansehen.

Die Trennung der Rollen soll die Anwendung übersichtlicher machen. Ein Helfer benötigt andere Funktionen als eine Person, die einen Auftrag erstellt. Deshalb sollen Benutzer nur die Seiten aufrufen können, die zu ihrer Rolle gehören.

## Aufträge erstellen und ansehen

Die Aufträge bilden den Mittelpunkt unserer Anwendung. Eine hilfesuchende Person beschreibt, welche Unterstützung benötigt wird. Zusätzlich können Angaben zur Aufgabe, zum ungefähren Ort, zum erwarteten Zeitaufwand und zur Bezahlung gemacht werden.

Ein neuer Auftrag erhält zunächst den Status `offen`. Er erscheint anschließend in der Übersicht der Helfer.

Die Auftragsübersicht soll einfach aufgebaut sein. Ein Helfer soll schnell erkennen können:

- worum es bei der Aufgabe geht,
- in welchem Gebiet sie stattfindet,
- wie der hilfesuchende heißt und wie alt er ist

Die vollständige Adresse muss in dieser Übersicht noch nicht angezeigt werden.

## Auftrag annehmen

Entscheidet sich ein Helfer für eine Aufgabe, kann er den Auftrag annehmen. Dabei wird der Auftrag mit dem Benutzerkonto des Helfers verbunden und der Status wird von `offen` auf `angenommen` geändert.

Danach wird der Auftrag nicht mehr als frei verfügbar angezeigt. So soll verhindert werden, dass mehrere Helfer denselben Auftrag gleichzeitig übernehmen.

Der angenommene Auftrag erscheint anschließend auf der persönlichen Seite **Meine Aufträge**. Dort sieht der Helfer nur die Aufträge, die ihm selbst zugeordnet wurden.

## Nachrichten und Terminvereinbarung

Nicht jede Einzelheit lässt sich bereits beim Erstellen eines Auftrags festlegen. Deshalb gehört eine Nachrichtenfunktion zu unserer Lösung.

Nach der Annahme können Helfer und hilfesuchende Person zum Beispiel besprechen:

- wann die Aufgabe durchgeführt wird,
- wie lange sie voraussichtlich dauert,
- wo genau das Treffen stattfindet,
- welche Hilfsmittel benötigt werden,
- was genau erledigt werden soll.

Wenn beide Seiten einen passenden Zeitpunkt gefunden haben, kann der Termin in der Anwendung gespeichert werden. Der Termin ist dem Auftrag und den beteiligten Benutzern zugeordnet.

Wir haben uns bewusst dafür entschieden, Chat und Termin erst nach der Annahme eines Auftrags zu ermöglichen. Dadurch kann nicht jeder Benutzer ohne Zusammenhang private Nachrichten an andere Personen senden.

## Sicherheit

Sicherheit war in unserer Umfrage eines der am häufigsten genannten Themen. Mehrere Teilnehmer wünschten sich eine Möglichkeit, besser einschätzen zu können, mit wem sie einen Auftrag durchführen.

Für den ersten Prototyp sind deshalb folgende Punkte vorgesehen:

- Benutzer müssen angemeldet sein,
- Funktionen werden abhängig von der Rolle freigegeben,
- Aufträge werden eindeutig einem Benutzer zugeordnet,
- persönliche Aufträge sind nur für den jeweiligen Benutzer sichtbar,
- Nachrichten dürfen nur von den beteiligten Personen gelesen werden,
- vollständige Adressen werden nicht öffentlich angezeigt,
- Passwörter werden nicht als normaler Text gespeichert.

Das Bundesamt für Sicherheit in der Informationstechnik empfiehlt, Onlinekonten durch sichere Passwörter und weitere Schutzmaßnahmen abzusichern.[5] Für eine spätere Version wären zusätzlich eine Identitätsprüfung, eine Meldefunktion und Bewertungen denkbar.

Diese Erweiterungen gehören allerdings nicht zum ersten Prototyp, weil zunächst der grundlegende Ablauf funktionieren soll.

## Einfache Bedienung

Da auch ältere Menschen zur Zielgruppe gehören, soll die Anwendung nicht unnötig kompliziert sein. Die Navigation soll wenige und klar benannte Punkte enthalten. Formulare sollen nur Informationen abfragen, die für den jeweiligen Auftrag tatsächlich gebraucht werden.

Die BAGSO weist darauf hin, dass ältere Menschen ohne ausreichenden Zugang zum Internet oder ohne entsprechende digitale Erfahrung in vielen Bereichen auf Schwierigkeiten stoßen.[6] Deshalb wollen wir möglichst auf komplizierte Menüs, lange Texte und schwer verständliche Begriffe verzichten.

Für den Prototyp bedeutet das unter anderem:

- gut erkennbare Schaltflächen,
- eindeutige Beschriftungen,
- wenige Eingabefelder pro Formular,
- eine übersichtliche Navigation,
- unterschiedliche Ansichten für Helfer und Hilfesuchende,
- verständliche Rückmeldungen nach einer Aktion.

## Geplanter Ablauf

Der wichtigste Ablauf der Anwendung sieht folgendermaßen aus:

1. Eine hilfesuchende Person registriert sich und meldet sich an.
2. Sie erstellt einen neuen Auftrag.
3. Der Auftrag wird als `offen` gespeichert.
4. Ein Helfer meldet sich an und öffnet die Auftragsübersicht.
5. Er wählt einen passenden Auftrag aus und nimmt ihn an.
6. Der Auftrag erhält den Status `angenommen`.
7. Der Auftrag erscheint unter **Meine Aufträge**.
8. Helfer und hilfesuchende Person klären die Einzelheiten im Chat.
9. Ein gemeinsamer Termin wird gespeichert.
10. Nach der Durchführung kann der Auftrag abgeschlossen werden.

Dieser Ablauf ist gleichzeitig der Happy Path unseres ersten Prototyps.

## Abgrenzung

HelpYourNeighbour soll keine professionelle Pflege ersetzen. Die Plattform ist nur für einfache Alltagshilfen vorgesehen.

Nicht über die Anwendung vermittelt werden sollen beispielsweise:

- medizinische Behandlungen,
- die Verabreichung von Medikamenten,
- Wundversorgung,
- professionelle Körperpflege,
- Tätigkeiten, für die eine pflegerische Ausbildung erforderlich ist,
- Aufgaben, bei denen eine besondere Gefahr für die beteiligten Personen besteht.

Die Bezahlung über Leistungen der Pflegeversicherung ist ebenfalls nicht Bestandteil des ersten Prototyps. Für solche Leistungen gelten besondere Voraussetzungen und teilweise landesrechtliche Anerkennungsverfahren.

## Ideen für spätere Erweiterungen

Während der Planung sind weitere Ideen entstanden, die in einer späteren Version umgesetzt werden könnten:

- gegenseitige Bewertungen,
- Verifizierung von Benutzerkonten,
- Suche nach Entfernung oder Stadtteil,
- Filter nach Art der Aufgabe,
- Benachrichtigungen über neue Aufträge,
- Anzeige bereits abgeschlossener Aufträge.

Für die erste Version konzentrieren wir uns jedoch auf Registrierung, Benutzerrollen, Aufträge, Annahme, Nachrichten und Termine.


## Quellen

[1] Deutsches Zentrum für Altersfragen:  
„Doppelbelastung ohne Entlastung? Herausforderungen und gesetzliche Maßnahmen für die Vereinbarkeit von Pflege und Beruf in einer alternden Gesellschaft“, 2024.  
https://www.dza.de/fileadmin/dza/Dokumente/DZA_Aktuell/DZA-Aktuell_03_2024_Vereinbarkeit_fin.pdf

[2] Zentrum für Qualität in der Pflege:  
„Pflegende Angehörige in Deutschland“.  
https://www.zqp.de/schwerpunkt/pflegende-angehoerige/

[3] Deutsches Zentrum für Hochschul- und Wissenschaftsforschung und Deutsches Studierendenwerk:  
„Die Studierendenbefragung in Deutschland: 22. Sozialerhebung“.  
https://www.studierendenwerke.de/fileadmin/user_upload/22._Soz_Hauptbericht_barrierefrei.pdf

[4] Eigene Google-Forms-Umfrage zu den Erwartungen potenzieller Helfer:  
https://docs.google.com/forms/d/e/1FAIpQLScVY0u_WoM7r9eHBA584PHetlEOEdd927fDkLNXmvmM_PN0Bg/viewform?usp=header

[5] Bundesamt für Sicherheit in der Informationstechnik:  
„Basistipps zur IT-Sicherheit“.  
https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/cyber-sicherheitsempfehlungen_node.html

[6] BAGSO – Bundesarbeitsgemeinschaft der Seniorenorganisationen:  
„Leben ohne Internet – geht’s noch?“.  
https://www.bagso.de/themen/digitalisierung/leben-ohne-internet/


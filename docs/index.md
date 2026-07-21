# HelpYourNeighbour

HelpYourNeighbour ist eine webbasierte Vermittlungsplattform, die hilfsbedürftige Menschen mit engagierten Helferinnen und Helfern verbindet. Pflegebedürftige Personen können Unterstützungsaufträge erstellen, während Helfer offene Aufträge ansehen und sich darauf bewerben können. Nach der Annahme einer Bewerbung stehen beiden Personen eine Terminverwaltung und ein integrierter Chat zur Verfügung. Zusätzlich prüft ein Administrator neu registrierte Nutzer und kann Helfer nach der Kontrolle ihres Führungszeugnisses freigeben.

## Sample App Screen

<img width="1108" height="499" alt="image" src="https://github.com/user-attachments/assets/b703dfad-d87a-495d-9141-b581c6b303bc" />


## Improvements / Refinements since First Submission

Seit der First Submission wurden mehrere zentrale Funktionen ergänzt und bestehende Abläufe verbessert.

### Upload eines Führungszeugnisses

Helfer müssen bei der Registrierung ein Führungszeugnis als PDF-Datei hochladen. Die Datei wird gespeichert und kann anschließend durch einen Administrator in der Nutzerübersicht geprüft werden. Erst nach der Prüfung und Freigabe erhält der Helfer Zugriff auf die geschützten Funktionen der Plattform.

Diese Erweiterung unterstützt das Vertrauen und die Sicherheit innerhalb der Plattform, da Helfer vor der Vermittlung überprüft werden können.

### Bewerbungen auf Aufträge

In der ersten Version konnten Helfer einen offenen Auftrag direkt annehmen. Dieser Ablauf wurde durch ein Bewerbungsverfahren ersetzt.

Helfer können sich nun auf offene Aufträge bewerben. Die pflegebedürftige Person erhält eine Übersicht über alle Bewerbungen und kann die Vorstellungstexte sowie weitere Informationen der Helfer ansehen. Anschließend kann eine Bewerbung angenommen oder abgelehnt werden.

Abgelehnte Bewerbungen werden als abgelehnt markiert. Sobald eine Bewerbung angenommen wird, wird der ausgewählte Helfer dem Auftrag zugeordnet und die übrigen Bewerbungen des Auftrags werden gelöscht.

Diese Änderung stärkt die Entscheidungsfreiheit der pflegebedürftigen Person und richtet die Anwendung deutlicher an der Value Proposition aus.

### Chatverlauf löschen

Für den integrierten Chat wurde eine Soft-Delete-Funktion ergänzt. Nutzer können ihren eigenen Chatverlauf leeren, ohne dass die Nachrichten vollständig aus der Datenbank gelöscht werden.

Dabei wird für jede Nachricht getrennt gespeichert, ob sie für den Sender oder den Empfänger gelöscht wurde. Dadurch kann ein Nutzer einen Chat ausblenden, während der andere Nutzer den bisherigen Verlauf weiterhin sehen kann.

Wird der zugehörige Auftrag gelöscht, bleiben bereits geschriebene Nachrichten absichtlich erhalten. Der bisherige Chatverlauf kann weiterhin angesehen werden, neue Nachrichten können danach jedoch nicht mehr gesendet werden.

### Aufträge bearbeiten und löschen

Pflegebedürftige Personen können ihre veröffentlichten Aufträge nachträglich bearbeiten oder vollständig löschen.

Beim Bearbeiten können die Wohnsituation und die Beschreibung des Unterstützungsbedarfs aktualisiert werden. Beim Löschen wird der Auftrag aus der Datenbank entfernt.

Bereits vorhandene Termine und Nachrichten werden dabei absichtlich nicht gelöscht. Dadurch bleiben vergangene Termine und bereits geführte Kommunikation weiterhin nachvollziehbar. Termine, deren Auftrag gelöscht wurde, können anschließend nicht mehr bearbeitet werden. Auch das Schreiben neuer Nachrichten ist nach dem Löschen des zugehörigen Auftrags nicht mehr möglich.

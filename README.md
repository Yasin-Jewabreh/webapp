# 🤝 HelpYourNeighbour

Eine webbasierte Vermittlungsplattform (Two-Sided Platform), die pflegebedürftige Menschen mit engagierten Helfern (Studenten, Schülern und Azubis) verbindet. 

Entwickelt im Rahmen des Moduls "Full-Stack Web Development".

---

## 💡 Value Proposition

**Das Problem:**
In Deutschland gibt es über 5,7 Millionen Pflegebedürftige (Tendenz steigend). Viele dieser Menschen haben Anspruch auf Pflege- und Entlastungsleistungen, machen diese aber nicht geltend – oft aus Unwissenheit oder weil keine Angehörigen in der Nähe sind. Gleichzeitig suchen viele junge Menschen (Studenten, Schüler, Azubis ab 18 Jahren) nach flexiblen Nebenjobs, um den steigenden Lebenshaltungskosten entgegenzuwirken, finden aber oft keine Tätigkeit, die sich mit ihrem Zeitplan vereinbaren lässt.

**Unsere Lösung:**
*HelpYourNeighbour* schließt diese Lücke. Die Plattform ermöglicht es pflegebedürftigen Personen (PP), unkompliziert Alltagshilfe (Haushalt, Einkaufen, Gesellschaft) anzufragen. Junge Helfer können diese Aufträge flexibel annehmen, sich sozial engagieren und gleichzeitig Geld verdienen. 

---

## ✨ Features (Core Scope)

* **Zwei-Rollen-System:** Getrennte Dashboards und Logiken für Pflegebedürftige und Helfer.
* **Auftragsmanagement:** Pflegebedürftige können Hilfe anfragen; Helfer können offene Aufträge in ihrer Umgebung einsehen und annehmen.
* **Integriertes Chat-System:** Direkte, datenbankgestützte Kommunikation zwischen Helfer und Pflegebedürftigem zur Terminabsprache.
* **Privacy / Soft-Delete:** Chatverläufe können einseitig gelöscht werden (analog zu WhatsApp), ohne die Datenbankintegrität zu verletzen.
* **Sichere Authentifizierung:** Login-System mit gehashten Passwörtern und Session-Management.

---

## 🛠️ Tech Stack & Constraints

Dieses Projekt wurde streng nach den Vorgaben des Moduls entwickelt. **Es wurde vollständig auf den Einsatz von custom JavaScript/TypeScript verzichtet.** Alle UI-Updates und Interaktionen basieren auf Jinja2 Server-Side-Rendering und klassischem HTTP-Routing.

* **Backend:** Python 3, Flask
* **Datenbank:** SQLite (Nutzung einer einzigen lokalen `.db` Datei)
* **ORM:** Flask-SQLAlchemy (Modern SQLAlchemy 2.0 Syntax)
* **Frontend:** HTML5, CSS3, Jinja2 Template-Engine
* **Styling:** Bootstrap 5 (Pulse Theme via Flask-Bootstrap)
* **Formulare & Auth:** Flask-WTF, WTForms, Flask-Login

---

## 🚀 Installation & Setup (Local Development)

Das Projekt ist nativ auf Windows und macOS lauffähig. Es werden keine Container (Docker) benötigt.

**1. Repository klonen**
```bash
git clone [HIER_EUREN_GITHUB_LINK_EINFÜGEN]
cd webapp

2. Virtuelle Umgebung erstellen und aktivieren

Windows: python -m venv venv
  venv\Scripts\activate

  Mac/Linux: python3 -m venv venv
  source venv/bin/activate

  3. Abhängigkeiten installieren

pip install -r requirements.txt

4. Datenbank generieren & Server starten
Die SQLite-Datenbank (helpyourneighbour.db) wird beim ersten Start der Applikation automatisch im Ordner generiert.

python app.py
# oder: flask run

Die App ist nun unter http://127.0.0.1:5000 im Browser erreichbar.

👥 Das Team & Contributions
Jedes Teammitglied hat signifikant zum Erfolg dieses Projekts beigetragen. Die individuelle Aufgabenverteilung gliederte sich wie folgt:

Mohamed: Architektur des Frontends und UI/UX-Design mittels zentraler base.html (siehe DD-04). Konzeption und Implementierung der empfängerspezifischen Chat-Routenstruktur (/chat/<int:empfaenger_id>) sowie des zugrundeliegenden Datenbankmodells für Nachrichten inklusive dynamischem Zeitzonen-Management via pytz (siehe DD-05).

Yavuz: Backend-Logik für das Auftragsmanagement, Session-Management und sichere Verknüpfung von erstellten Aufträgen mit dem eingeloggten Nutzer zur Sicherstellung der Datenintegrität (siehe DD-01).

Yasin: Konzeption und Implementierung des erweiterten Datenmodells für die Registrierung (siehe DD-02). Abwägung zwischen User Experience und Plattform-Sicherheit bei der Erfassung von Nutzerdaten und Validierung (WTForms).

Salih: Scope-Management und Anforderungsanalyse für das MVP (siehe DD-03). Strategische Ausrichtung der Kernfunktionen, Definition der Value Proposition für die Two-Sided Platform und grundlegende Dokumentation.

(Detaillierte Design-Entscheidungen und Mockups befinden sich im /docs Verzeichnis).

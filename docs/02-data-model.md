---
title: Data Model
nav_order: 2
---

{: .no_toc }
# Data Model

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Übersicht

Das Datenmodell der Anwendung besteht aus den vier zentralen Entitäten **Nutzer**, **Auftrag**, **Nachricht** und **Termin**. Nutzer können Aufträge erstellen, Nachrichten austauschen und Termine im Zusammenhang mit einem Auftrag vereinbaren.

## Entity Relationship Diagram

![Datenmodell](assets/images/erm-datenmodell.png)

## Beschreibung der Entitäten

### Nutzer

Speichert die Informationen registrierter Benutzer.

Wichtige Attribute:
- id
- vorname
- nachname
- email
- telefonnummer
- passwort

### Auftrag

Beschreibt eine Hilfsanfrage, die von einem Nutzer erstellt wird.

Wichtige Attribute:
- id
- titel
- beschreibung
- erstellt_am
- nutzer_id

### Nachricht

Ermöglicht die Kommunikation zwischen zwei Nutzern.

Wichtige Attribute:
- id
- sender_id
- empfaenger_id
- inhalt
- zeitstempel

### Termin

Repräsentiert einen vereinbarten Termin zu einem Auftrag.

Wichtige Attribute:
- id
- datum
- uhrzeit
- auftrag_id

## Beziehungen

- Ein Nutzer kann mehrere Aufträge erstellen.
- Ein Nutzer kann mehrere Nachrichten senden und empfangen.
- Ein Auftrag kann einen oder mehrere Termine besitzen.
- Ein Termin gehört genau zu einem Auftrag.
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

<img width="451" height="486" alt="image" src="https://github.com/user-attachments/assets/c224a16f-6101-46cb-b7e1-8d503b30d611" />

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

- Ein Nutzer kann keinen oder mehrere Aufträge erstellen bzw. annehmen.
- Ein Nutzer kann keine mehrere Nachrichten senden und empfangen.
- Ein Auftrag kann keinen oder mehrere Termine besitzen.
- Ein Termin gehört genau zu einem Auftrag.

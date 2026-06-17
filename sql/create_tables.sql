DROP TABLE IF EXISTS auftraege;

CREATE TABLE auftraege (
    id Integer PRIMARY KEY AUTOINCREMENT
    hilfsart TEXT NOT NULL,
    datum TEXT NOT NULL,
    uhrzeit TEXT NOT NULL,
    dauer REAL NOT NULL,
    adresse TEXT NOT NULL,
    beschreibung TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'offen'
);
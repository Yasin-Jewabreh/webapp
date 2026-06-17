
CREATE TABLE nutzer (
    nutzer_id Integer PRIMARY KEY AUTOINCREMENT,
    vorname TEXT NOT NULL,
    nachname TEXT NOT NULL, 
    geburtsdatum TEXT NOT NULL,
    straße TEXT NOT NULL,
    hausnummer Integer NOT NULL,
    postleitzahl Integer NOT NULL,
    ort TEXT NOT NULL,
    helfer BOOLEAN NOT NULL
);


CREATE TABLE auftraege (
    auftrags_id Integer PRIMARY KEY AUTOINCREMENT,
    nutzer_id Integer,
    vorname TEXT,
    hilfsart TEXT NOT NULL,
    adresse TEXT NOT NULL,
    beschreibung TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'offen',
    FOREIGN KEY (nutzer_id) REFERENCES nutzer (nutzer_id)
    FOREIGN KEY (vorname) REFERENCES nutzer (vorname)
);


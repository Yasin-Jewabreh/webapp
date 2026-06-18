
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

CREATE TABLE auftrag (
    auftrags_id Integer PRIMARY KEY AUTOINCREMENT,
    nutzer_id Integer PRIMARY KEY,
    vorname TEXT,
    adresse TEXT NOT NULL,
    beschreibung TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'offen',
    FOREIGN KEY (nutzer_id) REFERENCES nutzer (nutzer_id)
    FOREIGN KEY (vorname) REFERENCES nutzer (vorname)
);

CREATE TABLE termin (
    auftrags_id Integer,
    nutzer_id_helfer Integer PRIMARY KEY,
    nutzer_id_pp Integer PRIMARY KEY,
    datum TEXT NOT NULL,
    uhrzeit_beginn TEXT NOT NULL,
    uhrzeit_ende TEXT NOT NULL,
    FOREIGN KEY (nutzer_id_helfer) REFERENCES nutzer (nutzer_id) ON DELETE CASCADE,
    FOREIGN KEY (nutzer_id_pp) REFERENCES nutzer (nutzer_id) ON DELETE CASCADE
);


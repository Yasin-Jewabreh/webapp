import click
import os
import sqlite3
from flask import current_app, g

def get_db_con(pragma_foreign_keys=True):
    if "db_con" not in g:
        g.db_con = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES #bestimmte Datentypen werden besser gelesen wie DATE und TIMESTAMP
        )
        g.db_con.row_factory = sqlite3.Row #row["name"] statt row[2]

        if pragma_foreign_keys:
            g.db_con.execute("PRAGMA foreign_keys = ON;")#Check Up ob der Datensatz richtig ist user=5 hat auftrag gibt es user 5?

    return g.db_con


def close_db_con(e=None): #Definierung einer DB schließung 
    db_con = g.pop("db_con", None) #Hol db_con raus aus g falls keine verbindung wird "None" ausgegeben

    if db_con is not None:
        db_con.close()

@click.command("init-db")
def init_db():
    
    os.makedirs(current_app.instance_path, exist_ok=True)
    
    db_con = get_db_con()

    with current_app.open_resource("Pflegehilfe/drop_table.sql") as f:
        db_con.executescript(f.read().decode("utf-8"))

    with current_app.open_resource("Pflegehilfe/create_tables.sql") as f:
        db_con.executescript(f.read().decode("utf-8"))

    click.echo("Database has been initialized")

def init_app(app):
    app.teardown_appcontext(close_db_con)
    app.cli.add_command(init_db)
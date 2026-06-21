from app import app, db, Auftrag

with app.app_context():
    db.session.query(Auftrag).delete()
    db.session.commit()
    print("Alle erstellten Aufträge wurden erfolgreich gelöscht!")
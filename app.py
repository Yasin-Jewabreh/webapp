from datetime import date, time, datetime
from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap5
import forms

app = Flask(__name__)

from db import db
from models import Termin, Nutzer, Auftrag, Nachricht

app.config["SECRET_KEY"] = "secret_key_just_for_dev_environment"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bootstrap = Bootstrap5(app)


@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/termine/", methods = ["GET", "POST"])
def termine():
    form = forms.TerminErstellenForm()

    aktueller_nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.rolle == "PP")).scalars().first()

    if aktueller_nutzer.rolle == "Helfer":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]

    elif aktueller_nutzer.rolle == "PP":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]

    if aktueller_nutzer.rolle == "Helfer":
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif aktueller_nutzer.rolle == "PP":
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
   
    form.teilnehmer.choices.insert(0,(0, "---Bitte wählen---"))

    if request.method == "GET":
        return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= aktueller_nutzer)
    else:
        if "erledigen_id" in request.form:
            termin_id = int(request.form.get("erledigen_id"))
            termin = db.session.get(Termin,termin_id)
            if termin:
                termin.complete = True
                db.session.commit()
                flash("Termin als erledigt markiert!", "success")
            return redirect(url_for("termine"))
        
        if "bestaetigen_id" in request.form:
            termin_id = int(request.form.get("bestaetigen_id"))
            termin = db.session.get(Termin,termin_id)
            if termin:
                termin.bestaetigt = True
                db.session.commit()
                flash("Termin erfolgreich bestätigt!", "success")
            return redirect(url_for("termine"))
       
        if "ablehnen_id" in request.form:
            termin_id = int(request.form.get("ablehnen_id"))
            termin = db.session.get(Termin,termin_id)
            if termin:
                db.session.delete(termin)  
                db.session.commit()
                flash("Termin abgelehnt!", "warning")
            return redirect(url_for("termine"))

        if form.validate():

            gewaehlter_auftrag_id = int(form.teilnehmer.data)
            auftrag = db.session.get(Auftrag, gewaehlter_auftrag_id)

            ueberschneidung = db.session.execute(db.select(Termin).where(
                Termin.datum == form.datum.data,
                Termin.complete == False,
                (Termin.helfer_id == auftrag.helfer_id)| (Termin.pp_id == auftrag.pp_id),
                Termin.uhrzeit_beginn < form.uhrzeit_ende.data,
                Termin.uhrzeit_ende > form.uhrzeit_beginn.data)).scalars().first()

            if ueberschneidung:
                    flash("Fehler: Zu dieser Uhrzeit gibt es eine Terminüberschneidung!", "danger")
                    return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= aktueller_nutzer)
            termin = Termin(helfer_id = auftrag.helfer.id,
                            auftrag_id = auftrag.id,
                            pp_id = auftrag.pp_id,
                            notizen = form.notizen.data, 
                            datum=form.datum.data, 
                            uhrzeit_beginn = form.uhrzeit_beginn.data, 
                            uhrzeit_ende = form.uhrzeit_ende.data,
                            ersteller_id = aktueller_nutzer.id                                                       
                            )
            db.session.add(termin)
            db.session.commit()
            flash("Termin wurde eingetragen.", "success")
            return redirect(url_for("termine"))
        else:
            flash("Der Termin konnte leider nicht eingetragen werden", "warning")
        return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= aktueller_nutzer)


@app.route('/termine/<int:id>', methods=['GET', 'POST'])
def termin(id):
    termin = db.session.get(Termin, id) 
    form = forms.TerminBearbeiternForm(obj=termin)
    
    aktueller_nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.rolle == "PP")).scalars().first()

    if aktueller_nutzer.rolle == "Helfer":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname}") for a in verfuegbare_auftraege]

    elif aktueller_nutzer.rolle == "PP":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]

    if request.method == 'GET':
        if termin:
            return render_template('termin-bearbeiten.html', form=form)
        else:
            abort(404)
    else:
        if form.speichern.data == True:
            if form.validate():
                form.populate_obj(termin)
                
                gewaehlter_auftrag_id = int(form.teilnehmer.data)
                auftrag = db.session.get(Auftrag, gewaehlter_auftrag_id)

                ueberschneidung = db.session.execute(db.select(Termin).where(
                    Termin.id != id,
                    Termin.datum == form.datum.data,
                    Termin.complete == False,
                    (Termin.helfer_id == auftrag.helfer_id)| (Termin.pp_id == auftrag.pp_id),
                    Termin.uhrzeit_beginn < form.uhrzeit_ende.data,
                    Termin.uhrzeit_ende > form.uhrzeit_beginn.data)).scalars().first()

                if ueberschneidung:
                    flash("Fehler: Zu dieser Uhrzeit gibt es eine Terminüberschneidung!", "danger")
                    return redirect(url_for('termin', id=id))
                termin.auftrag_id= gewaehlter_auftrag_id
                termin.pp_id = auftrag.pp.id
                termin.helfer_id = auftrag.helfer.id
                termin.bestaetigt = False
                termin.ersteller_id = aktueller_nutzer.id
                db.session.add(termin)
                db.session.commit()
                flash("Deine Änderungen wurden erfolgreich gespeichert", "success")
                return redirect(url_for('termine'))
            else:
                flash("Deine Änderungen konnten leider nicht gespeichert werden!", "warning")
            return render_template('termin-bearbeiten.html', form=form)
        elif form.entfernen.data == True:
            db.session.delete(termin)  
            db.session.commit()
            flash("Der Termin wurde erfolgreich gelöscht!", "success")
            return redirect(url_for('termine'), 303)
        elif form.zurueck.data == True:
            return redirect(url_for('termine'))
        else:
            flash("Nichts passiert", "info")
            return redirect(url_for('termin', id=id))
        

if __name__ == "__main__":
    app.run(debug=True)
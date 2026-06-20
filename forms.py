from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, TimeField, HiddenField
from wtforms.validators import InputRequired, Optional, ValidationError
from datetime import date


def check_datum(self, field):
        if field.data:
            if field.data.year < date.today().year or  field.data.year > date.today().year +1 :
                raise ValidationError(f"Das Datum muss im Jahr {date.today().year} oder {date.today().year +1} liegen!")

def check_uhrzeit(self, field):
        if self.uhrzeit_beginn.data and field.data:
            if field.data <= self.uhrzeit_beginn.data:
                raise ValidationError("Die End-Uhrzeit muss nach der Start-Uhrzeit liegen!")
            
class TerminErstellenForm(FlaskForm):
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int, validators=[InputRequired()])
    datum = DateField("Am",validators=[InputRequired(), check_datum], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired()],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired(), check_uhrzeit], format='%H:%M')
    notizen = StringField("Trage hier deine Notizen ein",validators=[Optional()])
    eintragen = SubmitField("Termin eintragen")

class TerminBearbeiternForm(FlaskForm):
    id = HiddenField()
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int, validators=[InputRequired()])
    datum = DateField("Am",validators=[InputRequired(), check_datum], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired()],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired(), check_uhrzeit], format='%H:%M')
    notizen = StringField("Trage hier deine Notizen ein",validators=[Optional()])
    speichern = SubmitField("Änderungen Speichern")
    entfernen = SubmitField("Termin löschen")
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, DateField, TimeField
from wtforms.validators import InputRequired, Length, Optional

class TerminErstellenForm(FlaskForm):
    auftrag_id = SelectField("Der Termin ist mit:", coerce=int, validators=[InputRequired()])
    datum = DateField("Am",validators=[InputRequired()], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired()])
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired()])
    notizen = StringField("Trage hier deine Notizen ein",validators=[Optional()])
    eintragen = SubmitField("Termin eintragen")

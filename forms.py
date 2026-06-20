from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields import DateField, TimeField
from wtforms.widgets import DateInput, TimeInput
from wtforms.validators import InputRequired, Optional

class TerminErstellenForm(FlaskForm):
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int, validators=[InputRequired()])
    datum = DateField("Am",validators=[InputRequired()], widget = DateInput(), format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von", widget = TimeInput(),validators=[InputRequired()],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",widget= TimeInput(),validators=[InputRequired()], format='%H:%M')
    notizen = StringField("Trage hier deine Notizen ein",validators=[Optional()])
    eintragen = SubmitField("Termin eintragen")

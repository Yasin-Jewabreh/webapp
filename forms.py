from datetime import date
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, DateField, HiddenField, SubmitField, SelectField, TextAreaField, BooleanField, EmailField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length, InputRequired, ValidationError)

class RollenWahlForm(FlaskForm):
    helfer_btn = SubmitField('Hilfe anbieten')
    suchender_btn = SubmitField('Hilfe suchen')

class RegisterForm(FlaskForm):

    vorname = StringField('Vorname', validators=[DataRequired(message="Bitte Vornamen eingeben.")])
    nachname = StringField('Nachname', validators=[DataRequired(message="Bitte Nachnamen eingeben.")])
    geschlecht = SelectField("Geschlecht",choices=[('männlich', 'Männlich'), ('weiblich', 'Weiblich'), ('divers', 'Divers')],validators=[DataRequired(message="Bitte Geschlecht eingeben.")])
    geburtsdatum = DateField('Geburtsdatum', format='%Y-%m-%d', validators=[DataRequired(message="Bitte Geburtsdatum auswählen.")])
    adresse = StringField('Adresse', validators=[DataRequired(message="Bitte Adresse eingeben.")])
    plz = StringField('PLZ', validators=[DataRequired(message="Bitte PLZ eingeben."), Length(min=5, max=5, message="PLZ muss 5-stellig sein.")])
    ort = StringField("Ort", validators=[DataRequired(message="Bitte Ort eingeben.")])
    email = StringField('E-Mail', validators=[DataRequired(message="Bitte E-Mail eingeben."), Email(message="Ungültige E-Mail-Adresse.")])
    telefonnummer = StringField('Telefonnummer', validators=[DataRequired(message="Bitte Telefonnummer eingeben.")])
    
    passwort = PasswordField('Passwort', validators=[
        DataRequired(message="Bitte Passwort eingeben."),
        Length(min=6, message="Das Passwort muss mindestens 6 Zeichen lang sein.")
    ])
    passwort2 = PasswordField('Passwort bestätigen', validators=[
        DataRequired(message="Bitte Passwort bestätigen."),
        EqualTo('passwort', message='Passwörter müssen übereinstimmen.')
    ])
    
    rolle = HiddenField('Rolle')
    submit = SubmitField('Registrieren')
class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[
        DataRequired(message="Bitte geben Sie Ihre E-Mail-Adresse ein."),
        Email(message="Ungültige E-Mail-Adresse.")
    ])
    passwort = PasswordField('Passwort', validators=[
        DataRequired(message="Bitte geben Sie Ihr Passwort ein.")
    ])
    submit = SubmitField('Login')    
class AuftragFormular(FlaskForm):
    wohnsituation = SelectField(
        "Wohnsituation",
        choices=[
            ("", "Bitte auswählen"),
            ("Ich lebe allein", "Ich lebe allein"),
            ("Ich lebe mit meinem Partner oder meiner Partnerin", "Ich lebe mit meinem Partner oder meiner Partnerin"),
            ("Ich lebe mit meiner Familie", "Ich lebe mit meiner Familie"),
            ("Ich lebe in einer Wohngemeinschaft", "Ich lebe in einer Wohngemeinschaft"),
            ("Ich lebe in einer Pflegeeinrichtung", "Ich lebe in einer Pflegeeinrichtung"),
            ("Andere Wohnsituation", "Andere Wohnsituation")
        ],
        validators=[DataRequired(message="Bitte wähle deine Wohnsituation aus.")]
    )

    beschreibung = TextAreaField(
        "Über mich",
        validators=[
            DataRequired(message="Bitte erzähle etwas über dich."),
            Length(max=500, message="Die Beschreibung darf maximal 500 Zeichen lang sein.")
        ]
    )
    
    bestaetigung = BooleanField(
        "Ich bestätige, dass die angegebenen Informationen sichtbar sein dürfen.",
        validators=[DataRequired(message="Du musst der Bestätigung zustimmen.")]
    )
    
    submit = SubmitField("Auftrag veröffentlichen")

def check_geburtsdatum(form, field):
    if field.data:
        if ((date.today() - field.data).days / 365.25) < 18:
            raise ValidationError(
                "Du musst mindestens 18 Jahre alt sein."
            )

class ProfilFormular(FlaskForm):
    vorname = StringField('Vorname', validators=[DataRequired(message="Bitte Vornamen eingeben.")])
    nachname = StringField('Nachname', validators=[DataRequired(message="Bitte Nachnamen eingeben.")])
    email = StringField('E-Mail', validators=[DataRequired(message="Bitte E-Mail eingeben."), Email(message="Ungültige E-Mail.")])
    telefon = StringField('Telefonnummer', validators=[DataRequired(message="Bitte Telefonnummer eingeben.")])
    adresse = StringField('Adresse', validators=[DataRequired(message="Bitte Adresse eingeben.")])
    plz = StringField('PLZ', validators=[DataRequired(message="Bitte PLZ eingeben.")])
    ort = StringField('Ort', validators=[DataRequired(message="Bitte Ort eingeben.")])
    submit = SubmitField('Änderungen speichern')
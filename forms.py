from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class AuftragFormular(FlaskForm):
    wohnsituation = SelectField("Wohnsituation",
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
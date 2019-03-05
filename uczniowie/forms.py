# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, BooleanField
from wtforms import SelectField, FormField, FieldList
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    nazwa = StringField('Nazwa klasy:', validators=[Required(message=blad1)])
    roknaboru = StringField('Rok naboru:', validators=[Required(message=blad1)])
    rokmatury = StringField('Rok matury:', validators=[Required(message=blad1)])


class UczenForm(FlaskForm):
    id = HiddenField("Uczeń id")
    imie = StringField('Imię:', validators=[Required(message=blad1)])
    nazwisko = StringField('Nazwisko:', validators=[Required(message=blad1)])
    plec = SelectField('Płeć:', coerce=int)
    klasa = SelectField('Klasa', coerce=int)

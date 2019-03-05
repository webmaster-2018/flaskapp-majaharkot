# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')

@app.route('/uczen_lista')
def uczen_lista():
    """Lista uczniów"""
    uczniowie = Uczen.select()
    return render_template('uczen_lista.html', uczniowie = uczniowie)
    
@app.route('/klasa_lista')
def klasa_lista():
    """Lista klas"""
    klasy = Klasa.select()
    return render_template('klasa_lista.html', klasy = klasy)

@app.route('/uczen_dodaj')
def uczen_dodaj():
    """Dodawanie ucznia"""
    form = UczenForm()
    
    if form.validate_on_submit():
        u = Uczen(imie=form.imie.data, 
                  nazwisko=form.nazwisko.data,
                  plec=form.plec.data,
                  klasa=form.klasa.data)
        u.save()
        
        flash('Dodano ucznia: {} {}'.format(form.imie.data, form.nazwisko.data))
        return redirect(url_for('uczen_lista'))
    
    return render_template('uczen_dodaj.html', form=form)
    
def get_or_404(uid):
    try:
        u = Uczen.get_by_id(uid)
        return u
    except Uczen.DoesNotExist:
        abort(404)

@app.route('/klasa_dodaj')
def klasa_dodaj():
    """Dodawanie klasa"""
    form = KlasaForm()
    
    if form.validate_on_submit():
        k = Klasa(nazwa=form.nazwa.data, 
                  roknaboru=form.roknaboru.data,
                  rokmatury=form.rokmatury.data)
        k.save()
        
        flash('Dodano klasę: {}'.format(form.nazwa.data))
        return redirect(url_for('klasa_lista'))
    
    return render_template('klasa_dodaj.html', form=form)

#!/usr/bin/env python 

from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
db = SQLAlchemy(app)

class Teams(db.Model):
    id = db.Column(db.String(length=5), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    barcode = db.Column(db.String(length=8), nullable=False, unique=True)
    manager = db.Column(db.String(length=15), nullable=False, unique=True)
    networth = db.Column(db.Float(), nullable=False)
    location = db.Column(db.String(length=15), nullable=False, unique=True)
    founded = db.Column(db.Integer(), nullable=False)

## basic introduction 
# @app.route("/")
# def hello_world():
#     return "<h1>Hello ballers! Am Felix. Welcome to my football fanbase</h1>"

# @app.route("/about/<username>") ## change this to a dynamic route 
# def about_page(username): 
#     return f"<h1>About Page for the {username} </h1>" 

## styling and templates 
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

## sending data to templates 
@app.route("/Teams")
def teams_page():
    premier_league_teams = [
    {
        "name": "Manchester City",
        "manager": "Pep Guardiola",
        "custom_id": "MNC",
        "custom_barcode": "MNC-2324",
        "first_eleven": ["Ederson", "Cancelo", "Dias", "Akanji", "Ake", "Rodri", "De Bruyne", "Gundogan", "Grealish", "Haaland", "Foden"],
        "net_worth": 1.5,
        "location": "Manchester, England",
        "founded": 1880
    },
    {
        "name": "Arsenal FC",
        "manager": "Mikel Arteta",
        "custom_id": "ARS",
        "custom_barcode": "ARS-2324",
        "first_eleven": ["Ramsdale", "Zinchenko", "Gabriel", "Saliba", "White", "Partey", "Odegaard", "Saka", "Martinelli", "Jesus", "Xhaka"],
        "net_worth": 1.2,
        "location": "London, England",
        "founded": 1886
    },
    {
        "name": "Liverpool FC",
        "manager": "Jürgen Klopp",
        "custom_id": "LIV",
        "custom_barcode": "LIV-2324",
        "first_eleven": ["Alisson", "Alexander-Arnold", "Van Dijk", "Konate", "Robertson", "Fabinho", "Thiago", "Salah", "Diaz", "Nunez", "Firmino"],
        "net_worth": 1.3,
        "location": "Liverpool, England",
        "founded": 1892
    },
    {
        "name": "Aston Villa",
        "manager": "Unai Emery",
        "custom_id": "AVL",
        "custom_barcode": "AVL-2324",
        "first_eleven": ["Martinez", "Cash", "Konsa", "Mings", "Digne", "Kamara", "McGinn", "Ramsey", "Buendia", "Watkins", "Bailey"],
        "net_worth": 0.8,
        "location": "Birmingham, England",
        "founded": 1874
    },
    {
        "name": "Tottenham Hotspur",
        "manager": "Ange Postecoglou",
        "custom_id": "TOT",
        "custom_barcode": "TOT-2324",
        "first_eleven": ["Lloris", "Romero", "Dier", "Davies", "Emerson", "Hojbjerg", "Bissouma", "Kulusevski", "Son", "Kane", "Richarlison"],
        "net_worth": 1.1,
        "location": "London, England",
        "founded": 1882
    },
    {
        "name": "Chelsea FC",
        "manager": "Mauricio Pochettino",
        "custom_id": "CHE",
        "custom_barcode": "CHE-2324",
        "first_eleven": ["Mendy", "Koulibaly", "Silva", "Chilwell", "James", "Fernandez", "Kovacic", "Mount", "Sterling", "Havertz", "Pulisic"],
        "net_worth": 1.4,
        "location": "London, England",
        "founded": 1905
    },
    {
        "name": "Newcastle United",
        "manager": "Eddie Howe",
        "custom_id": "NEW",
        "custom_barcode": "NEW-2324",
        "first_eleven": ["Pope", "Trippier", "Schar", "Botman", "Burn", "Joelinton", "Guimaraes", "Almiron", "Saint-Maximin", "Wilson", "Isak"],
        "net_worth": 0.9,
        "location": "Newcastle upon Tyne, England",
        "founded": 1892
    },
    {
        "name": "Manchester United",
        "manager": "Erik ten Hag",
        "custom_id": "MUN",
        "custom_barcode": "MUN-2324",
        "first_eleven": ["De Gea", "Wan-Bissaka", "Varane", "Maguire", "Shaw", "Casemiro", "Eriksen", "Fernandes", "Rashford", "Martial", "Sancho"],
        "net_worth": 750000000,
        "location": "Manchester, England",
        "founded": 1878
    },
    {
        "name": "West Ham United",
        "manager": "David Moyes",
        "custom_id": "WHU",
        "custom_barcode": "WHU-2324",
        "first_eleven": ["Fabianski", "Coufal", "Zouma", "Ogbonna", "Cresswell", "Rice", "Soucek", "Bowen", "Fornals", "Benrahma", "Antonio"],
        "net_worth": 550000000,
        "location": "London, England",
        "founded": 1895
    },
    {
        "name": "Crystal Palace",
        "manager": "Roy Hodgson",
        "custom_id": "CRY",
        "custom_barcode": "CRY-2324",
        "first_eleven": ["Guaita", "Clyne", "Guehi", "Andersen", "Mitchell", "Doucoure", "Eze", "Olise", "Zaha", "Edouard", "Ayew"],
        "net_worth": 450000000,
        "location": "London, England",
        "founded": 1905
    }
]
    return render_template('teams.html', teams=premier_league_teams)
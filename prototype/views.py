import sqlite3
from flask import Flask, request
from flask import render_template
from . import app

import os

@app.route("/")
def home():
    rows = list_all()

    return render_template('home.html', rows=rows)

#-------------------- SEARCHING SEARCH PAGES --------------------------
@app.route('/search', methods = ['POST', 'GET'])
def search():
    con = sqlite3.connect("bottle_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    if request.method == 'POST':
        object = request.form['search_scholarship_value']
    
        # BUILD QUERY
        query = "SELECT * FROM bottles WHERE object='" + object.lower() + "'"
        try:
            cur.execute(query)
        except: 
            print("Error occured when executing query")

        rows = list(cur.fetchall())
        con.close()
    
    else: 
        cur.execute("select * from bottles")
        rows = list(cur.fetchall())
        con.close()

    return render_template('home.html', rows=rows)

#Print all from database to terminal
def list_all():
    # if os.path.isfile("prototype/static/databases/scholarship_database.db"):
    #     con = sqlite3.connect("prototype/static/databases/scholarship_database.db")

    # path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') +"/static/databases/bottle_database.db"
    # if os.path.isfile(path):
    #     con = sqlite3.connect(path)
    
    con = sqlite3.connect("bottle_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    if request.method == 'POST':
        object = request.form['search_scholarship_value']
    
        # BUILD QUERY
        query = "SELECT * FROM bottles WHERE object='" + object + "'"
        try:
            cur.execute(query)
        except: 
            print("Error occured when executing query")

        rows = list(cur.fetchall())
        con.close()
    
    else: 
        cur.execute("select * from bottles")

        rows = list(cur.fetchall())
        con.close()

    return rows


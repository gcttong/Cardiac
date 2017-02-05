from __future__ import print_function
from flask import Flask, render_template, redirect, \
url_for, request, session, flash, g
import sys

import sqlite3
app = Flask(__name__)
app.database = "sample.db"


@app.route('/')
def main():
    return render_template('signup.html')
    #return redirect(url_for('info', name='Bob Wo', contact='Eddie Wang', phone='16479808401'))
    #return redirect(url_for('info', name='eddie', contact='gary', phone=16479808401))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        g.db = connect_db()
        victim = str(request.form['inputName'])
        contact = str(request.form['inputContact'])
        phone = str(request.form['inputPhone'])
        g.db.execute('insert into contacts values (?, ?, ?)', (victim, contact, phone))
        g.db.commit()
        g.db.close()
        return redirect(url_for('qr'))
    return render_template('signup.html')


@app.route('/qr', methods=['GET', 'POST'])
def qr():
    g.db = connect_db()
    cur = g.db.execute('select * from contacts')
    posts = [dict(victim=row[0], contact=row[1], phone=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('qr.html', posts=posts, crazy='/qresults')

@app.route('/info/<name><contact><phone>', methods=['GET', 'POST'])
def info(name, contact, phone):
    return render_template('info.html', mylist = [name,contact,phone])

@app.route('/qresults', methods=['GET','POST'])
def qresults():
    #address = "66 Wellington St W, Toronto, ON"
    posts = [dict(victim="Lily",contact="Jerry",phone="6479808401")]
    return render_template('qresults.html',posts=posts)

def connect_db():
    return sqlite3.connect(app.database)
    
if __name__ == '__main__':
    app.run(debug=True)

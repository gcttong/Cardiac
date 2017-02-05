from flask import Flask, render_template, redirect, \
url_for, request, session, flash, g

import sqlite3

app = Flask(__name__)
app.database = "sample.db"


@app.route('/')
def main():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #error = None
    if request.method == 'POST':
        #if len(str(request.form['inputPhone'])) != 10:
        #    error = 'Invalid credentials'
        #else:
        return redirect(url_for('qr'))
    return redirect(url_for('qr'))
    #else:
        #return redirect(url_for('qr'))
        #return render_template('signup.html')

@app.route('/qr', methods=['GET', 'POST'])
def qr():
    g.db = connect_db()
    cur = g.db.execute('select * from contacts')
    posts = [dict(victim=row[0], contact=row[1], phone=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('qr.html', posts=posts, crazy=str(3))

'''@app.route('/info', methods=['GET', 'POST'])
def info():
    '''
def connect_db():
    return sqlite3.connect(app.database)
    
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect 
import os
import sqlite3

app = Flask(__name__)
DB_PATH = 'data/gym.db'

os.makedirs('data', exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                     excercise TEXT, weight REAL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
@app.route('/')
def index():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT * FROM workouts ORDER BY date DESC')
        workouts = cursor.fetchall()
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])
def add():
    excercise = request.form['excercise']
    weight = request.form.get['weight']
    if excercise and weight:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('INSERT INTO workouts (excercise, weight) VALUES (?, ?)', (excercise, weight))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
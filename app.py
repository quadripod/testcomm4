from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            active_listening INTEGER,
            teamwork_communication INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, active_listening, teamwork_communication) VALUES (?, 0, 0)', (name,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_student/<int:student_id>', methods=['POST'])
def update_student(student_id):
    active_listening = request.form['active_listening']
    teamwork_communication = request.form['teamwork_communication']
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students 
        SET active_listening = ?, teamwork_communication = ?
        WHERE id = ?
    ''', (active_listening, teamwork_communication, student_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

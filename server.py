from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from openaiSudoku import loadSudokuDataFromFile
from sudoku import solveSudoku
from waitress import serve
import os
import copy


app = Flask(__name__)
app.secret_key = 'sudokey'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

def get_db_connection():
    conn = sqlite3.connect('sudoku.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return render_template('index.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if user already exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            flash('Użytkownik już istnieje')
            return redirect(url_for('reister'))
        
        # Register new user
        hashed_password = generate_password_hash(password)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

        conn.commit()
        conn.close()

        flash('Rejestracja zakończona pomyślnie. Możesz się zalogować.')
        return redirect(url_for('login'))
    # elif request.method == 'POST':
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if user exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            session['user_id'] = user['id']
            flash('Zalogowano')
            return redirect(url_for('index'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    flash('Wylogowano pomyślnie')
    return redirect(url_for('index'))

@app.route('/solve', methods=['POST'])
def solve():
    if 'username' not in session:
        flash('Musisz się zalogować')
        return redirect(url_for('login'))
    
    try:
        if 'sudoku_image' in request.files:
            # File uploaded
            file = request.files['sudoku_image']

            if file.filename == '':
                return render_template('index.html', error='Nie wybrano pliku')
            
            filename = secure_filename(file.filename)

            
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            img = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            sudoku_data=loadSudokuDataFromFile(file)

            matrix = eval(sudoku_data)

            
            print(matrix)
            # SOlove
            if solveSudoku(matrix):
                # Save solution in history
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('''
                        INSERT INTO sudoku_history (user_id, sudoku_data, solved_data)
                               VALUES (?, ?, ?)
                ''', (session['user_id'], str(sudoku_data), str(matrix)))
                conn.commit()
                conn.close()

                return render_template('index.html', sudoku=matrix, solved=True, image_url=img, username=session['username'])
            else:
                return render_template('index.html', error="This sudoku cannot be solved", sudoku=matrix, image_url=img, username=session['username'])

        else:
            
            # Text data formular

            sudoku_data = []

            for i in range(9):
                row = []
                for j in range(9):
                    cell_value = request.form.get(f'cell-{i}-{j}') #get cell value from form data
                    row.append(int(cell_value) if cell_value else 0) #if empty - make 0
                sudoku_data.append(row)

            solved_sudoku = copy.deepcopy(sudoku_data)
            
            if solveSudoku(solved_sudoku):
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('''
                        INSERT INTO sudoku_history (user_id, sudoku_data, solved_data)
                               VALUES (?, ?, ?)
                ''', (session['user_id'], str(sudoku_data), str(solved_sudoku)))
                conn.commit()
                conn.close()

                return render_template('index.html', sudoku=solved_sudoku, solved=True, username=session['username'])
            else:
                return render_template('index.html', error="This sudoku cannot be solved", sudoku=solved_sudoku, username=session['username'])
                

    except Exception as e:
        # Zaloguj błąd (możesz użyć logging zamiast print)
        print(f"Wystąpił błąd: {e}")
        return render_template('index.html', error="Wystąpił błąd podczas rozwiązywania sudoku.", username=session['username'])

@app.route('/history')
def history():
    if 'username' not in session:
        flash('Musisz się zalogować')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Get history for logged user
        cursor.execute('''
                SELECT * FROM sudoku_history
                    WHERE user_id = ?
                    ORDER BY timestamp DESC
        ''', (session['user_id'],))
        rows = cursor.fetchall()

        history = []
        for row in rows:
            entry = dict(row)  # Konwersja sqlite3.Row na zwykły słownik
            entry['sudoku_data'] = eval(entry['sudoku_data'])  # Zamiana stringa na listę
            entry['solved_data'] = eval(entry['solved_data'])  # Zamiana stringa na listę
            history.append(entry)  # Dodanie przekształconego rekordu do listy


    except Exception as e:
        print(f"Błąd: {e}")
        history = []
    finally:
        conn.close()

    
    # conn.close()

    return render_template('history.html', history=history, username=session['username'])




if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    serve(app, host="0.0.0.0", port=8000)
    
# @app.route('/weather')
# def get_weather():
#     city = request.args.get('city')

#     if not bool(city.strip()):
#         # You could render "City Not Found" instead like we do below
#         city = "Kansas City"

#         # City is not found by API
#     # if not weather_data['cod'] == 200:
#     #     return render_template('city-not-found.html')

#     weather_data = get_current_weather(city)

#     return render_template(
#         "weather.html",
#         title=weather_data["name"],
#         status=weather_data["weather"][0]["description"].capitalize(),
#         temp=f"{weather_data['main']['temp']:.1f}",
#         feels_like=f"{weather_data['main']['feels_like']:.1f}"
#     )

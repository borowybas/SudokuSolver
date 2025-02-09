import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    # Create connection with database SQLite
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Połączono z bazą danych: {db_file}")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    # Create tables in database
    try:
        cursor = conn.cursor()

        # User table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT NOT NULL UNIQUE,
                       password TEXT NOT NULL
                       )
        ''')

        # Solvings history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sudoku_history (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTEGER NOT NULL,
                       sudoku_data TEXT NOT NULL,
                       solved_data TEXT NOT NULL,
                       timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                       FOREIGN KEY (user_id) REFERENCES users (id)
                       )
        ''')

        conn.commit()
        conn.close()
        print("Tabele utworzone pomyślnie.")
    except Error as e:
        print(e)

if __name__ == "__main__":
    # Create connection with database
    conn = create_connection("sudoku.db")
    # Create tables
    if conn is not None:
        create_tables(conn)
    else:
        print("Błąd podczas łączenia z bazą danych")

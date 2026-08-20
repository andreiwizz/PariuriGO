import sqlite3

def init_db():
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS ponturi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meci TEXT NOT NULL,
            competitie TEXT NOT NULL,
            pronostic TEXT NOT NULL,
            cota REAL NOT NULL,
            ziua TEXT NOT NULL,
            status TEXT DEFAULT 'În așteptare'
        )
    ''')
    conn.commit()
    conn.close()

def adauga_pont(meci, competitie, pronostic, cota, ziua):
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO ponturi (meci, competitie, pronostic, cota, ziua)
        VALUES (?, ?, ?, ?, ?)
    ''', (meci, competitie, pronostic, cota, ziua))
    conn.commit()
    conn.close()

def get_ponturi(ziua):
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute("SELECT meci, competitie, pronostic, cota, status FROM ponturi WHERE ziua = ?", (ziua,))
    date = c.fetchall()
    conn.close()
    return date
# Adaugă această funcție în baza.py pentru a gestiona utilizatorii
def init_db_users():
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS utilizatori (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            plan TEXT DEFAULT 'Gratuit',
            data_expirare DATE
        )
    ''')
    conn.commit()
    conn.close()

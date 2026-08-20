import sqlite3

def init_db():
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    # Tabel pentru ponturi
    c.execute('''
        CREATE TABLE IF NOT EXISTS ponturi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meci TEXT, 
            competitie TEXT, 
            pronostic TEXT, 
            cota REAL, 
            ziua TEXT
        )
    ''')
    # Tabel pentru utilizatori si abonamente
    c.execute('''
        CREATE TABLE IF NOT EXISTS utilizatori (
            email TEXT PRIMARY KEY,
            abonament TEXT DEFAULT 'Niciunul',
            status_platit INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def adauga_pont(meci, competitie, pronostic, cota, ziua):
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute("INSERT INTO ponturi (meci, competitie, pronostic, cota, ziua) VALUES (?, ?, ?, ?, ?)",
              (meci, competitie, pronostic, cota, ziua))
    conn.commit()
    conn.close()

def get_ponturi(ziua):
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute("SELECT meci, competitie, pronostic, cota FROM ponturi WHERE ziua = ?", (ziua,))
    data = c.fetchall()
    conn.close()
    return data

def salveaza_user(email, abonament="Niciunul", platit=0):
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO utilizatori (email, abonament, status_platit) VALUES (?, ?, ?)",
              (email, abonament, platit))
    conn.commit()
    conn.close()

def verfica_acces(email):
    conn = sqlite3.connect("betgo.db")
    c = conn.cursor()
    c.execute("SELECT status_platit, abonament FROM utilizatori WHERE email = ?", (email,))
    res = c.fetchone()
    conn.close()
    return res if res else (0, "Niciunul")

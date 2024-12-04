import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('database/user_data.db')

def create_db():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    points INTEGER DEFAULT 10000,
                    level INTEGER DEFAULT 1,
                    exp INTEGER DEFAULT 0,
                    health INTEGER DEFAULT 100,
                    last_activity_time INTEGER)''')
    
    conn.commit()
    conn.close()

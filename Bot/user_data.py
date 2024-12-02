import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('database/user_data.db')

def create_db():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    points INTEGER,
                    level INTEGER,
                    exp INTEGER,
                    health_points INTEGER,
                    last_activity_time INTEGER)''')
    
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("INSERT INTO users (user_id, points, level, exp, health_points, last_activity_time) VALUES (?, ?, ?, ?, ?, ?)",
              (user_id, 10000, 1, 0, 100, 0))  # 100 health points placeholder
    
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    
    conn.close()
    return user

def update_user_data(user_id, new_exp, new_level):
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("UPDATE users SET exp=?, level=? WHERE user_id=?", (new_exp, new_level, user_id))
    
    conn.commit()
    conn.close()

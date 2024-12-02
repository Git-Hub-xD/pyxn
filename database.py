import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('user_data.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                user_id INTEGER PRIMARY KEY,
                                points INTEGER DEFAULT 10000,
                                level INTEGER DEFAULT 1,
                                exp INTEGER DEFAULT 0,
                                health INTEGER DEFAULT 100)''')
        self.conn.commit()

    def user_exists(self, user_id):
        self.cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        return self.cursor.fetchone() is not None

    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        self.conn.commit()

    def get_user_data(self, user_id):
        self.cursor.execute("SELECT points, level, exp, health FROM users WHERE user_id = ?", (user_id,))
        return self.cursor.fetchone()

    def update_user_activity(self, user_id, message):
        # Example: Increase points and exp based on messages
        self.cursor.execute("UPDATE users SET exp = exp + 1 WHERE user_id = ?", (user_id,))
        self.conn.commit()

    def is_spammer(self, user_id):
        # Check for spammy behavior (e.g., frequent messages)
        return False  # Implement your flood control logic here

    def close(self):
        self.conn.close()

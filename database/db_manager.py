import sqlite3
import os

# Path to the SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), "user_data.db")


# Connect to SQLite database
def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DB_PATH)


# Initialize the database schema
def create_db():
    """Initialize the database by creating tables."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            username TEXT,
                            points INTEGER DEFAULT 10000,
                            level INTEGER DEFAULT 1,
                            exp INTEGER DEFAULT 0,
                            health INTEGER DEFAULT 100,
                            last_activity_time INTEGER DEFAULT 0)''')
        conn.commit()
        print("Database initialized successfully.")


# Add a new user to the database
def add_user(user_id, username="Unknown"):
    """Add a new user to the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO users (user_id, username, points, level, exp, health, last_activity_time)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, username, 10000, 1, 0, 100, 0),
        )
        conn.commit()


# Ensure the user exists in the database
def ensure_user_exists(user_id, username="Unknown"):
    """Ensure the user exists in the database. If not, add them."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT 1 FROM users WHERE user_id = ?",
            (user_id,),
        )
        if cursor.fetchone() is None:  # User doesn't exist
            add_user(user_id, username)  # Add the user using add_user


# Retrieve user data from the database
def get_user(user_id):
    """Retrieve user data from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT user_id, username, points, level, exp, health, last_activity_time
            FROM users
            WHERE user_id = ?
            """,
            (user_id,),
        )
        return cursor.fetchone()


# Update user points
def update_points(user_id, points):
    """Update user points."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users
            SET points = points + ?
            WHERE user_id = ?
            """,
            (points, user_id),
        )
        conn.commit()


# Update user level and experience
def update_level(user_id, level, exp):
    """Update user level and experience."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users
            SET level = ?, exp = ?
            WHERE user_id = ?
            """,
            (level, exp, user_id),
        )
        conn.commit()


# Update user health points
def update_health(user_id, health):
    """Update user health points."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users
            SET health = ?
            WHERE user_id = ?
            """,
            (health, user_id),
        )
        conn.commit()

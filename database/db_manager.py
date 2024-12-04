import sqlite3
import os

API_ID = "21989020"
API_HASH = "3959305ae244126404702aa5068ba15c"
BOT_TOKEN = "7410194228:AAGyVEIgppL2tusKBIG_f-PI0XMwuD4uY1Y"

app = Client(
  name="pyxn",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN

# Path to the SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), "user_data.db")

# List of allowed group chat IDs
ALLOWED_GROUPS = [-1002135192853, -1002324159284]  # Replace with your actual group IDs

@app.on_message(filters.text)
def track_messages(client, message):
    if message.chat.id not in ALLOWED_GROUPS:
        return  # Don't track if the message is not from an allowed group

    # Your existing message tracking logic...

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def create_db():
    """Initialize the database by creating tables."""
    with connect_db() as conn:
        with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as schema_file:
            conn.executescript(schema_file.read())
        print("Database initialized successfully.")

def add_user(user_id, username):
    """Add a new user to the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO users (user_id, username)
            VALUES (?, ?)
            """,
            (user_id, username),
        )
        conn.commit()

def get_user(user_id):
    """Retrieve user data from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT user_id, username, points, level, exp, health
            FROM users
            WHERE user_id = ?
            """,
            (user_id,),
        )
        return cursor.fetchone()

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

def ensure_user_exists(user_id, username=None):
    """Ensure the user exists in the database. If not, add them."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT 1 FROM users WHERE user_id = ?",
            (user_id,),
        )
        if cursor.fetchone() is None:  # User doesn't exist
            cursor.execute(
                """
                INSERT INTO users (user_id, username)
                VALUES (?, ?)
                """,
                (user_id, username or "Unknown"),
            )
            conn.commit()

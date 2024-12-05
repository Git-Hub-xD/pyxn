-- Create a table to store user data
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,       -- Unique Telegram user ID
    username TEXT,                     -- Telegram username
    points INTEGER DEFAULT 10000,      -- Starting points
    level INTEGER DEFAULT 1,           -- User level
    exp INTEGER DEFAULT 0,             -- Experience points
    health INTEGER DEFAULT 100,        -- Health points
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user joined
);
CREATE TABLE IF NOT EXISTS group_settings (
    group_id INTEGER PRIMARY KEY,
    custom_welcome TEXT DEFAULT NULL,
    custom_goodbye TEXT DEFAULT NULL,
    welcome_enabled INTEGER DEFAULT 1,
    goodbye_enabled INTEGER DEFAULT 1
);

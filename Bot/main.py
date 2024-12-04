from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot.user_data import create_db, add_user, get_user
from Bot.flood_control import check_flood
from Bot.leveling import level_up
from database.db_manager import ensure_user_exists, get_user, update_points, update_level, update_health

API_ID = "21989020"
API_HASH = "3959305ae244126404702aa5068ba15c"
BOT_TOKEN = "7410194228:AAGyVEIgppL2tusKBIG_f-PI0XMwuD4uY1Y"

app = Client(
  name="pyxn",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

# Create DB on bot startup
create_db()

@app.on_message(filters.command("start"))
def start_handler(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name  # Use first name for the link
    username = message.from_user.username or first_name

    # Ensure user exists in the database
    ensure_user_exists(user_id, username)

    # Fetch user data from the database
    user_data = get_user(user_id)
    if user_data:
        user_id, username, points, level, exp, health = user_data

      # Create a user link using the user's first name
        user_link = f'<a href="tg://user?id={user_id}">{first_name}</a>'

      # Inline keyboard with a button to your chat group
        chat_group_url = "https://t.me/KaisenWorld"  # Replace with your group link
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Join Chat Group", url=chat_group_url)]
            ]
        )

        # Send a welcome message with user data and the user link
        message.reply_photo(
            photo="https://imgur.com/a/hJU9sB4",
            caption=(
                f"Hey {user_link}, 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝖯𝗒𝗑𝗇 𝖡𝗈𝗍 ! 🎉\n\n"
                f"<b>📜 ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴛᴏᴋᴇɴs ?</b>\n"
                f"- ᴊᴜsᴛ ᴄʜᴀᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ! ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ʏᴏᴜ sᴇɴᴅ ɢᴇᴛs ʏᴏᴜ ᴄʟᴏsᴇʀ ᴛᴏ ᴇᴀʀɴɪɴɢ ᴋᴀɪᴢᴇɴ ᴛᴏᴋᴇɴs.\n\n"
                f"𝖦𝖾𝗍 𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝗇𝗈𝗐 ! 𝗍𝗒𝗉𝖾 /help 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌.\n\n"
                f"🎯 **ʏᴏᴜʀ sᴛᴀᴛs :**\n• ᴘᴏɪɴᴛs : {points}\n• ʟᴇᴠᴇʟ : {level}"
            ),
          reply_markup=keyboard,  # Attach the keyboard to the message
        )

    # If user data doesn't exist, add the user and fetch data again
    if user_data is None:
        add_user(user_id, username)
        user_data = get_user(user_id)


@app.on_message(filters.command("profile"))
def profile_handler(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name  # Use first name for the link
    username = message.from_user.username or message.from_user.first_name

    # Ensure user exists in the database
    ensure_user_exists(user_id, username)

    # Create a user link using the user's first name
    user_link = f'<a href="tg://user?id={user_id}">{first_name}</a>'
  
    # Fetch user data
    user_data = get_user(user_id)
    if user_data:
        user_id, username, points, level, exp, health = user_data
        message.reply_text(
            f"**{user_link}'s Profile :**\n"
            f"Points : {points}\n"
            f"Level: {level}\n"
            f"EXP : {exp}\n"
            f"Health : {health}"
        )
    else:
        message.reply_text("Error fetching your profile. Please try again later.")
@app.on_message(filters.text)
def handle_message(client, message):
    user_id = message.from_user.id
    if check_flood(user_id):
        message.reply("You are sending messages too quickly. Please wait a few seconds.")
    else:
        level_up(user_id, message.text)

# List of allowed group chat IDs
ALLOWED_GROUPS = [-1001234567890, -1009876543210]  # Replace with your actual group IDs

@app.on_message(filters.text)
def track_messages(client, message):
    if message.chat.id not in ALLOWED_GROUPS:
        return  # Don't track if the message is not from an allowed group

    # Your existing message tracking logic...

if __name__ == "__main__":
    app.run()

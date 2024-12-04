from pyrogram import Client, filters
from Bot.user_data import create_db, add_user, get_user
from Bot.flood_control import check_flood
from Bot.leveling import level_up
from database.db_manager import ensure_user_exists, get_user

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
    username = message.from_user.username or message.from_user.first_name

    # Ensure user exists
    ensure_user_exists(user_id, username)

      # Fetch user data
    user_data = get_user(user_id)
    if user_data:
        user_id, username, points, level, exp, health = user_data
      
    message.reply_photo(
photo="https://imgur.com/a/hJU9sB4",
      caption="𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝖯𝗒𝗑𝗇 𝖡𝗈𝗍 ! 🎉\n\n<b>➻ ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴛᴏᴋᴇɴs ?</b>\n- ᴊᴜsᴛ ᴄʜᴀᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ! ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ʏᴏᴜ sᴇɴᴅ ɢᴇᴛs ʏᴏᴜ ᴄʟᴏsᴇʀ ᴛᴏ ᴇᴀʀɴɪɴɢ ᴋᴀɪᴢᴇɴ ᴛᴏᴋᴇɴs.\n\n𝖦𝖾𝗍 𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝗇𝗈𝗐 ! 𝗍𝗒𝗉𝖾 /help 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾 𝖼ommands.\n\nYou have {points} points, level {level}, and {health} health points.")

    if user_data is None:
        add_user(user_id)
        user_data = get_user(user_id)


@app.on_message(filters.command("profile"))
def profile_handler(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name

    # Ensure user exists in the database
    ensure_user_exists(user_id, username)

    # Fetch user data
    user_data = get_user(user_id)
    if user_data:
        user_id, username, points, level, exp, health = user_data
        message.reply_text(
            f"**@{username}'s Profile :**\n"
            f"Points: {points}\n"
            f"Level: {level}\n"
            f"EXP: {exp}\n"
            f"Health: {health}"
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

if __name__ == "__main__":
    app.run()

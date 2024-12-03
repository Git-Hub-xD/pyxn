from pyrogram import Client, filters
from Bot.user_data import create_db, add_user, get_user
from Bot.flood_control import check_flood
from Bot.leveling import level_up

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
def start(client, message):
    user_id = message.from_user.id
    user_data = get_user(user_id)

    if user_data is None:
        add_user(user_id)
        user_data = get_user(user_id)

    message.reply_photo(
photo="https://imgur.com/a/hJU9sB4",
      caption="𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝖯𝗒𝗑𝗇 𝖡𝗈𝗍 ! 🎉\n\n<b>➻ ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴛᴏᴋᴇɴs ?</b>\n- ᴊᴜsᴛ ᴄʜᴀᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ! ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ʏᴏᴜ sᴇɴᴅ ɢᴇᴛs ʏᴏᴜ ᴄʟᴏsᴇʀ ᴛᴏ ᴇᴀʀɴɪɴɢ ᴋᴀɪᴢᴇɴ ᴛᴏᴋᴇɴs.\n\n𝖦𝖾𝗍 𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝗇𝗈𝗐 ! 𝗍𝗒𝗉𝖾 /help 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾 𝖼ommands.\n\nYou have {user_data[1]} points, level {user_data[2]}, and {user_data[4]} health points.")

@app.on_message(filters.command("profile"))
def profile(client, message):
    user_id = message.from_user.id
    user_data = get_user(user_id)

    if user_data:
        message.reply(f"Points: {user_data[1]}\nLevel: {user_data[2]}\nExp: {user_data[3]}\nHealth: {user_data[4]}")
    else:
        message.reply("You need to start the bot first using /start.")

@app.on_message(filters.text)
def handle_message(client, message):
    user_id = message.from_user.id
    if check_flood(user_id):
        message.reply("You are sending messages too quickly. Please wait a few seconds.")
    else:
        level_up(user_id, message.text)

if __name__ == "__main__":
    app.run()

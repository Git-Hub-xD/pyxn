from pyrogram import Client, filters
from database.db_manager import set_custom_message, toggle_message_status
from config.settings import BOT_ADMINS

# Restrict commands to bot admins
def bot_admin_only(func):
    def wrapper(client, message):
        if message.from_user.id not in BOT_ADMINS:
            message.reply_text("You are not authorized to use this command.")
            return
        return func(client, message)
    return wrapper

# Command to set a custom welcome message
@app.on_message(filters.command("setwelcome"))
@bot_admin_only
def set_welcome(client, message):
    group_id = message.chat.id
    custom_message = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None

    if not custom_message:
        message.reply_text("Please provide a custom welcome message.")
        return

    set_custom_message(group_id, "welcome", custom_message)
    message.reply_text(f"Custom welcome message set for this group:\n\n{custom_message}")

# Command to set a custom goodbye message
@app.on_message(filters.command("setgoodbye"))
@bot_admin_only
def set_goodbye(client, message):
    group_id = message.chat.id
    custom_message = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None

    if not custom_message:
        message.reply_text("Please provide a custom goodbye message.")
        return

    set_custom_message(group_id, "goodbye", custom_message)
    message.reply_text(f"Custom goodbye message set for this group:\n\n{custom_message}")

# Command to toggle welcome messages
@app.on_message(filters.command("togglewelcome"))
@bot_admin_only
def toggle_welcome(client, message):
    group_id = message.chat.id
    toggle = message.text.split(None, 1)[1].lower() if len(message.text.split()) > 1 else None

    if toggle not in ["on", "off"]:
        message.reply_text("Please specify 'on' or 'off'.")
        return

    status = 1 if toggle == "on" else 0
    toggle_message_status(group_id, "welcome", status)
    message.reply_text(f"Welcome messages are now {'enabled' if status else 'disabled'} for this group.")

# Command to toggle goodbye messages
@app.on_message(filters.command("togglegoodbye"))
@bot_admin_only
def toggle_goodbye(client, message):
    group_id = message.chat.id
    toggle = message.text.split(None, 1)[1].lower() if len(message.text.split()) > 1 else None

    if toggle not in ["on", "off"]:
        message.reply_text("Please specify 'on' or 'off'.")
        return

    status = 1 if toggle == "on" else 0
    toggle_message_status(group_id, "goodbye", status)
    message.reply_text(f"Goodbye messages are now {'enabled' if status else 'disabled'} for this group.")

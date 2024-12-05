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

# Default Welcome/goodbye setting 
@app.on_message(filters.new_chat_members)
def welcome_message(client, message):
    group_id = message.chat.id
    settings = get_group_settings(group_id)
    if not settings or not settings[2]:  # Check if welcome messages are enabled
        return

    custom_welcome = settings[0]
    for member in message.new_chat_members:
        if member.is_bot:
            continue

        user_link = f'<a href="tg://user?id={member.id}">{member.first_name}</a>'
        message.reply_text(
            custom_welcome or f"🎉 Welcome {user_link} to the group! 🎉\nType <code>/help</code> to explore all my features!",
            parse_mode="HTML"
        )

@app.on_message(filters.left_chat_member)
def goodbye_message(client, message):
    group_id = message.chat.id
    settings = get_group_settings(group_id)
    if not settings or not settings[3]:  # Check if goodbye messages are enabled
        return

    custom_goodbye = settings[1]
    member = message.left_chat_member
    if member.is_bot:
        return

    user_link = f'<a href="tg://user?id={member.id}">{member.first_name}</a>'
    message.reply_text(
        custom_goodbye or f"👋 {user_link} has left the group. We’ll miss you!",
        parse_mode="HTML"
    )

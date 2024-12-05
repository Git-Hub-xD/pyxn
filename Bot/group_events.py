from pyrogram import Client, filters
from database.db_manager import get_group_settings

# Welcome Message Handler
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

# Goodbye Message Handler
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

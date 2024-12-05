from Bot.main import app
from pyrogram import Client, filters

# Assuming your app instance is named `app`
@app.on_message(filters.command("help"))
async def help_handler(client, message):
    help_text = (
        "**Bot Help Menu**\n\n"
        "`/start` - Start the bot and get a welcome message.\n"
        "`/help` - Show this help message.\n"
        "`/daily` - Claim your daily rewards.\n"
        "`/level` - Check your current level and experience points.\n"
        "`/balance` - Check your current balance.\n"
        "`/shop` - Access the shop to redeem rewards.\n"
        "`/admin` - Admin-only commands (restricted access).\n"
        "\n*More commands will be added soon!*"
    )

    await message.reply_text(help_text)

# Run the bot (ensure the app instance is started)
if __name__ == "__main__":
    app.run()

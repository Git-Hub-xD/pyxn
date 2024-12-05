import time

@app.on_message(filters.command("daily"))
def daily_reward(client, message):
    user_id = message.from_user.id
    
    # Fetch user data
    user_data = get_user(user_id)
    if not user_data:
        message.reply("Error: User not found in the database.")
        return

    user_id, username, points, level, exp, health, last_claimed = user_data
    
    # Get the current time
    current_time = time.time()  # Get current time in seconds

    # Check if the user has already claimed their daily reward
    if last_claimed != 0:
        # Calculate the time difference between now and last claim
        time_difference = current_time - last_claimed

        # If less than 24 hours, the user can't claim again
        if time_difference < 86400:  # 86400 seconds = 24 hours
            remaining_time = 86400 - time_difference  # Time left to claim
            remaining_hours = remaining_time // 3600
            remaining_minutes = (remaining_time % 3600) // 60
            message.reply(f"You've already claimed your reward. Please wait {int(remaining_hours)} hours and {int(remaining_minutes)} minutes to claim again.")
            return

    # Daily reward amount
    DAILY_REWARD = 100
  
    # Give the user their daily reward
    new_points = points + DAILY_REWARD

    # Update the user's points and last claim time
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users
            SET points = ?, last_claimed = ?
            WHERE user_id = ?
            """,
            (new_points, current_time, user_id)
        )
        conn.commit()

    # Inform the user that they've successfully claimed their reward
    message.reply(f"🎉 You've successfully claimed your daily reward of {DAILY_REWARD} points! Your new point balance is {new_points}.")

# Run the bot (ensure the app instance is started)
if __name__ == "__main__":
    app.run()

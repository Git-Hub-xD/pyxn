from bot.user_data import get_user, update_user_data

# Placeholder: A simple way to gain experience (leveling up)
def level_up(user_id, message_text):
    user_data = get_user(user_id)
    
    if user_data:
        exp_gained = len(message_text.split())  # Exp based on message length (placeholder logic)
        new_exp = user_data[3] + exp_gained
        new_level = new_exp // 100  # Every 100 exp points for level up

        update_user_data(user_id, new_exp, new_level)
        print(f"User {user_id} leveled up to level {new_level} with {new_exp} exp.")

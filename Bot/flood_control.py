import time

user_last_command_time = {}

def check_flood(user_id):
    current_time = time.time()
    if user_id in user_last_command_time:
        last_time = user_last_command_time[user_id]
        if current_time - last_time < 1:  # 1 seconds cooldown
            return True
    user_last_command_time[user_id] = current_time
    return False

import re

def check_length(password):
    return len(password) >= 8

def check_score(password):
    score = 0
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[^a-zA-Z0-9]", password): score += 1
    return score >= 4

def is_not_leaked(password):
    file_path = '/home/sahal/Downloads/rockyou.txt'
    try:
        with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
            for line in f:
                if password == line.strip():
                    return False 
        return True
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}")
        return True

def main():
    print('''  _____                 _____ _               _             
    |  __ \               / ____| |             | |            
    | |__) |_ _ ___ ___  | |    | |__   ___  ___| | _____ _ __ 
    |  ___/ _` / __/ __| | |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | |  | (_| \__ \__ \ | |____| | | |  __/ (__|   <  __/ |   
    |_|   \__,_|___/___/  \_____|_| |_|\___|\___|_|\_\___|_|   ''')

    print('\n\n')
    password = input('ENTER YOUR PASSWORD : ')

    if not check_length(password):
        print("❌ Change Password: Need 8 or more characters.")
    elif not check_score(password):
        print("❌ You need to add at least one lowercase, uppercase, number, and special character.")
    elif not is_not_leaked(password):
        print("❌ Found in leaked password list! You must change this password.")
    else:
        print("✅ Password is strong and not found in leaked lists. You are good to go!")

# This was the part causing the error
if __name__ == "__main__":
    main()
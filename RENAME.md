# Pass Checker 🛡️

A Python-based password strength analyzer that checks for complexity and cross-references passwords against the famous **RockYou** breach list to ensure your credentials haven't been leaked.

## 🚀 Features
* **Length Validation:** Ensures passwords are at least 8 characters long.
* **Complexity Analysis:** Checks for uppercase, lowercase, numbers, and special characters.
* **Breach Check:** Scans a local copy of `rockyou.txt` to see if the password has appeared in historical data breaches.
* **Clean Interface:** Features a stylized ASCII art header.

## 🛠️ Requirements
* **Python 3.x**
* **RockYou Wordlist:** You will need a copy of `rockyou.txt`. 
  * *Linux users:* Usually found at `/usr/share/wordlists/rockyou.txt`.
  * *Others:* Can be downloaded from [Kaggle](https://www.kaggle.com/datasets/wjburns common-password-list-rockyoutxt) or GitHub.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sahal-thaha/passwordchecker.git
   cd passwordchecker
   python3 passwordchecker.py
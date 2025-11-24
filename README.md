# Termipass – Terminal Password Manager

TermiPass is a local, command-line password manager written in Python. It stores account credentials securely using strong encryption and protects access with a master password. The project is designed as a practical way to learn file handling, cryptography, modular programming, command-line interfaces, and real-world application development.

---

## Features

- Add, view, update, and delete account entries  
- All data stored in an encrypted local file  
- Requires a master password to unlock  
- Fully offline and does not send data anywhere  
- Graceful handling of invalid input and runtime errors  
- Modular and clean code structure

---

## How It Works

1. When launched, the program asks for the master password.
2. If an encrypted vault already exists:
   - The program attempts to decrypt it using the provided password.
   - Successful decryption loads the stored accounts.
   - Incorrect password denies access.
3. If no vault exists:
   - A new one is created and encrypted using the master password.
4. Any changes made are re-encrypted and saved securely to disk.

---

## Technology

- **Python 3**
- **JSON** for structured storage  
- **cryptography** library for AES encryption  
- Modular multi-file layout (`main.py`, `storage.py`, `crypto.py`, etc.)  
- Command-line interaction using menus or `argparse`

---

## 7-Day Development Roadmap

### Day 1 – Setup & Planning
- Create project structure and document requirements

### Day 2 – JSON Data Storage
- Implement add, view, update, delete operations  
- Save and load data from a JSON file

### Day 3 – Code Organization
- Split logic into separate modules  
- Improve error handling

### Day 4 – Encryption Layer
- Implement encryption and decryption with a master password

### Day 5 – Authentication
- Require the master password at startup

### Day 6 – User Experience Improvements
- Cleaner CLI interaction  
- Better validation and messages

### Day 7 – Final Testing & Debugging
- Test edge cases and correct issues

---

## Installation

```bash
git clone <repository-url>
cd vaultline
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt

![Preview](banner_AES.jpeg)


# 🔐 Military Data Security System with Python

This project is a simulation of a military-style data security system built using Python. It mimics a secure communication channel between a **commander** and a **troop**, utilizing encryption and token-based authentication.

---

## 🧰 Features

- ✅ **Message Encryption** using `Fernet` (symmetric encryption)
- 🔑 **Token-based Authentication** with `bcrypt`
- ⏰ **Time-limited Message Access**
- 🚫 **Handles Incorrect Token & Expired Messages**
- 🎓 **Python Educational Concepts Integrated**:
  - Conditionals & Looping
  - Data Structures (`list`, `set`, `tuple`, `dict`)
  - Lambda Functions
  - List & Dictionary Comprehension
  - Functions, Scoping, Recursion

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `main_user.py` | Komandan - Encrypt and send message |
| `main_pasukan.py` | Pasukan - Decrypt and verify message |
| `key.key` | Encryption key (auto-generated) |
| `data_rahasia.json` | Stores encrypted message data |
| `log_akses.txt` | Records all access attempts |

---

## 🚀 How to Run

1. **Install requirements** (if needed):
   ```bash
   pip install cryptography bcrypt colorama

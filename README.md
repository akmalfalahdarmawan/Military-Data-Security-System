🔐 Military Data Security System with Python
This project is a simulation of a military-style data security system built using Python. It mimics a secure communication channel between a commander and a troop, utilizing encryption and token-based authentication.

🧰 Key Features
Message Encryption: Uses Fernet (symmetric encryption) to secure secret messages.

Token-based Access: Messages can only be opened with a valid access token (hashed with bcrypt).

Time-Limited Access: Messages automatically expire after a defined period.

Error Handling: Handles incorrect tokens, expired messages, and invalid keys gracefully.

Educational Design: Integrates core Python concepts like:

Conditionals & loops

Data structures (list, set, tuple, dict)

Lambda functions

List/dictionary comprehension

Functions, scoping, and recursion

📁 Files Overview
main_user.py – Used by the commander to send encrypted messages.

main_pasukan.py – Used by the troop to access and decrypt the message.

key.key – Automatically generated encryption key.

data_rahasia.json – Stores encrypted message data.

log_akses.txt – Records every access attempt.

📚 Purpose
This project was created as part of a Python programming assignment. It is designed to demonstrate fundamental Python skills in a real-world simulation context while also introducing basic data security practices.

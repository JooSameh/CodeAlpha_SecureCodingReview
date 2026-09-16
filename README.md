# 🛡️ CodeAlpha - Secure Coding Review

## 📋 Task 3 Overview
This repository contains a manual code audit and remediation for a common web security vulnerability: **SQL Injection (SQLi)**. The task was completed as part of the Cyber Security Internship at CodeAlpha.

## 🔍 Audit Details
* **Target Language:** Python
* **Target Application:** A basic SQLite login authentication script.
* **Audit Method:** Manual Code Inspection.

## ⚠️ Vulnerability Found: SQL Injection
In the `vulnerable_login.py` script, the application is vulnerable to SQL Injection. 
**The Issue:** The code concatenates raw user input directly into the SQL query string using f-strings:
`query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"`

**Impact:** An attacker can input malicious SQL payloads (e.g., `' OR '1'='1`) to bypass authentication entirely without knowing the actual password.

## 🛠️ Remediation & Best Practices
To fix this vulnerability, I rewrote the authentication logic in `secure_login.py` using **Prepared Statements (Parameterized Queries)**.

**The Fix:**
`query = "SELECT * FROM users WHERE username = ? AND password = ?"`
`cursor.execute(query, (username, password))`

**Why it works:** By using `?` placeholders, the database treats the user's input strictly as string data, not as executable SQL commands. Even if a malicious payload is entered, it is safely neutralized.

## 📂 Repository Contents
1. `vulnerable_login.py`: The original script demonstrating the SQL Injection flaw.
2. `secure_login.py`: The patched, secure version using parameterized queries.

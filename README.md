# Security Audit: SQLite Authentication Module

**Prepared for:** CodeAlpha Cybersecurity Internship (Task 3)
**Vulnerability Focus:** SQL Injection (CWE-89)

## Audit Overview
This repository contains a manual source code review and remediation patch for an authentication mechanism susceptible to SQL Injection (SQLi). The audit focuses on identifying improper input sanitization and implementing industry-standard structural defenses.

## Vulnerability Assessment
*   **Target:** `vulnerable_login.py` (Python / SQLite3)
*   **Attack Vector:** Authentication Bypass via Tautology Payload.
*   **Root Cause:** The script dynamically constructs SQL execution strings using Python f-strings, directly concatenating untrusted user input into the database query logic.

**Vulnerable Implementation:**
```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

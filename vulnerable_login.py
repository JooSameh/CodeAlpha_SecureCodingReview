import sqlite3

def login_vulnerable(username, password):
    # In-memory DB for simulation purposes
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    
    # VULNERABILITY: Unsanitized string concatenation (CWE-89)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing raw query: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        print("[!] Login Successful! (Authentication Bypassed)")
    else:
        print("[-] Login Failed.")

if __name__ == "__main__":
    print("--- SQLi Simulation (Tautology Payload) ---")
    # Payload designed to manipulate query logic into a TRUE condition
    login_vulnerable("admin", "' OR '1'='1")

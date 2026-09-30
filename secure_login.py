import sqlite3

def login_secure(username, password):
    # In-memory DB for simulation purposes
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    
    # REMEDIATION: Prepared statements enforce query pre-compilation
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    # The SQLite engine safely binds parameters as literal data, not executable syntax
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        print("[+] Login Successful! (Authorized Access)")
    else:
        print("[*] Login Failed. (Malicious Payload Neutralized)")

if __name__ == "__main__":
    print("--- Secure Execution Simulation ---")
    # The same payload is now treated purely as a string, preventing the bypass
    login_secure("admin", "' OR '1'='1")

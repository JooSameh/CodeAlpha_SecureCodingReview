import sqlite3

def login_secure(username, password):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    
    # ✅ الكود الآمن باستخدام (Prepared Statements / Parameterized Queries)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing Secure Query...")
    
    # تمرير المدخلات كمتغيرات منفصلة لمنع الحقن
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login Successful!")
    else:
        print("Login Failed!")

# تجربة نفس الهجوم على الكود الآمن
print("--- SQL Injection Attack Simulation on Secure Code ---")
login_secure('admin', "' OR '1'='1")
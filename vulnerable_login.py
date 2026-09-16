import sqlite3

def login(username, password):
    # إنشاء اتصال بقاعدة البيانات (للتجربة)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    
    # ❌ الكود المصاب بالثغرة (دمج المدخلات مباشرة في الاستعلام)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing Query: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        print("Login Successful!")
    else:
        print("Login Failed!")

# مثال على هجوم SQL Injection
print("--- SQL Injection Attack Simulation ---")
# الهاكر بيدخل الكود ده بدل الباسورد عشان يتخطى تسجيل الدخول
login('admin', "' OR '1'='1")
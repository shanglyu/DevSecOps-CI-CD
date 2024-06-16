import sqlite3

# Kết nối tới CSDL
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Tạo bảng users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

# Thêm dữ liệu vào bảng users
cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('shanglyu', 'Y1lSyH3U3LjE54aRb7K8cI3RfDV7KfAf', 'ADMIN'))

conn.commit()
conn.close()
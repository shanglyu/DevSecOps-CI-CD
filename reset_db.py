import sqlite3

db = sqlite3.connect('users.db')

db.executescript(
'''
DELETE FROM users WHERE id != 1;
'''
)

db.commit()
db.close()

print('Successfully reset!')
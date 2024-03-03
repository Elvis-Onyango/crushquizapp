import sqlite3

sql = sqlite3.connect('database.db')

cursor = sql.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_responses (
                  id INTEGER PRIMARY KEY,
                  question_id INTEGER,
                  username TEXT,
                  color TEXT,
                  movie TEXT,
                  food TEXT,
                  place TEXT,
                  season TEXT,
                  animal TEXT,
                  sport TEXT,
                  hobby TEXT,
                  music TEXT,
                  book TEXT,
                  fear TEXT,
                  dream TEXT,
                  like_about_self TEXT,
                  like_about_me TEXT,
                  scale TEXT,
                  answer TEXT
                  )''')

def add_response(question_id,username, color, movie, food, place, season, animal, sport, hobby, music, book, fear, dream, like_about_self, like_about_me, scale, answer):
    cursor.execute('''INSERT INTO quiz_responses (question_id,username, color, movie, food, place, season, animal, sport, hobby, music, book, fear, dream, like_about_self, like_about_me, scale, answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (question_id, username, color, movie, food, place, season, animal, sport, hobby, music, book, fear, dream, like_about_self, like_about_me, scale, answer))

def added_responses():
    cursor.execute('SELECT * FROM quiz_responses')
    return cursor.fetchall()

sql.commit()
sql.close()

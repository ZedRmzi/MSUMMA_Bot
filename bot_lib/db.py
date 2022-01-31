import sqlite3


DB_PATH = "./data/db/database.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

def OpenUserDatabase():
    """Open database used with bot.py"""
    openUserCommand = """CREATE TABLE IF NOT EXISTS
    users(discordId TEXT PRIMARY KEY,
          firstName TEXT NOT NULL,
          lastName TEXT NOT NULL)"""

    cur.execute(openUserCommand)



def CloseDatabase():
    """Closes the database once done"""
    conn.commit
    conn.close

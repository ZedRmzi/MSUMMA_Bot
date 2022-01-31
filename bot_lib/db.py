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

def AddUser(discordId: str, firstName: str, lastName: str):
    """
    Add a member to the user relation.

    `discordId`:  `str` The discord id of the member to add
    `firstName`: `str` The first name of the member to add
    `lastName`: `str` The last name of the member to add
    """
    OpenUserDatabase()
    cur.execute("INSERT INTO users VALUES(?, ?, ?)", (str(discordId), firstName, lastName))
    CloseDatabase()

#@ SQLite comes embedded in python

import sqlite3

#create DB file if does not exist
conn = sqlite3.connect('music.sqlite')
#define file handle for DB
cur = conn.cursor()

def print_row():
    #print rows
    print('Tracks:')
    cur.execute('SELECT title, plays FROM Tracks ORDER BY title')
    for row in cur:
        print(row)
    print()

"""
Define table and tell it what columns it will contain
and what data types per column
"""

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

print("Database created")

#Insert into table (creates tuple pairs of title and plays

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('The Grudge', 1))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Lateralus', 9))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Refecttion', 11))

#write inserts
conn.commit()

print_row()

#Update row
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = "Lateralus"')

print_row()

#Delete from table
cur.execute('DELETE FROM Tracks WHERE plays < 100')

print_row()
cur.close()
conn.close()

# Working with SQLite3
import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Movies 
	(Title TEXT, Director TEXT, Year INT)"""
)

# ? Add rows to the Movies table
# cursor.execute("""INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)""")
famousFilms = [
    ("Pulp Fiction", "Quentin Tarantino", 1994),
    ("Back to the Future", "Robert Zemeckis", 1985),
    ("Moonrise Kingdom", "Wes Anderson", 2012),
]
# cursor.executemany("INSERT INTO Movies VALUES (?,?,?)", famousFilms)

# ? Query the Movies table
release_year = (1985,)
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchall())

# ? Update rows in the Movies table and close the connection
connection.commit()
connection.close()

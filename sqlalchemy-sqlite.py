import sqlalchemy

# ? Using SQLAlchemy with SQLite. echo=True logs to console engine activity.
engine = sqlalchemy.create_engine("sqlite:///movies.db", echo=True)

# ? Create a metadata object to hold the table schema.
metadata = sqlalchemy.MetaData()
movies_table = sqlalchemy.Table(
    "Movies",
    metadata,
    sqlalchemy.Column("title", sqlalchemy.Text),
    sqlalchemy.Column("director", sqlalchemy.Text),
    sqlalchemy.Column("year", sqlalchemy.Integer),
)
metadata.create_all(engine)

# ? Using with, the connection is automatically closed at the end of the block.
with engine.connect() as conn:
    for row in conn.execute(sqlalchemy.select(movies_table)):
        print(row)


# ? Challenge: Create a table called Users with some fictional users.
users_to_insert = [
    {
        "first_name": "One",
        "last_name": "User",
        "email_address": "one.user@gmail.com",
    },
    {
        "first_name": "Two",
        "last_name": "User",
        "email_address": "two.user@gmail.com",
    },
    {
        "first_name": "Three",
        "last_name": "User",
        "email_address": "three.user@hotmail.com",
    },
    {
        "first_name": "Four",
        "last_name": "User",
        "email_address": "four.user@hotmail.com",
    },
]

engine = sqlalchemy.create_engine("sqlite:///users.db", echo=True)

metadata = sqlalchemy.MetaData()
users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email_address", sqlalchemy.String),
)
metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)
    conn.commit()

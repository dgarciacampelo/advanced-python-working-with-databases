import mysql.connector as mysql
import os

# ? Get environment variables.
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_ROOT_PSW = os.environ.get("MYSQL_ROOT_PASSWORD")


def connect(db_name, host="localhost", username="root", password=MYSQL_ROOT_PSW):
    # print(f"Connecting to database: {db_name} using root password: {password}")
    try:
        return mysql.connect(
            host=host,
            user=username,
            password=password,
            database=db_name,
        )
    except mysql.Error as e:
        print(e)


def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute(
        """INSERT INTO projects(title, description) 
		VALUES (%s, %s)""",
        project_data,
    )
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)
    cursor.executemany(
        """INSERT INTO tasks(project_id, description) 
		VALUES(%s, %s)""",
        tasks_data,
    )


if __name__ == "__main__":
    db = connect(MYSQL_DATABASE)
    cursor = db.cursor()

    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)

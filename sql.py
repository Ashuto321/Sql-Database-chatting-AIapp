import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
""")

cursor.execute("INSERT INTO STUDENT VALUES('Ashutosh','Gen ai','A',90)")
cursor.execute("INSERT INTO STUDENT VALUES('Anupam','DGen ai','B',100)")
cursor.execute("INSERT INTO STUDENT VALUES('Evanjilin','powebi','A',86)")
cursor.execute("INSERT INTO STUDENT VALUES('Nidhi','webDEVOPers','A',50)")
cursor.execute("INSERT INTO STUDENT VALUES('Parshvi','powebi','A',35)")

connection.commit()
connection.close()

print("Student DB Created!")

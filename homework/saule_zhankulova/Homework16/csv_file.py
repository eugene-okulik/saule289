import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "..", "..", "eugene_okulik", "Lesson_16", "hw_data", "data.csv")
file_path = os.path.abspath(file_path)
print(file_path)

with open(file_path, newline='') as csvfile:
    file_data = csv.reader(csvfile)
    data = [tuple(row) for row in file_data]

cursor = db.cursor()
cursor.execute("""
               SELECT s.name,
                      s.second_name,
                      g.title,
                      b.title,
                      sub.title,
                      l.title,
                      m.value
               FROM students s
                        JOIN `groups` g ON s.group_id = g.id
                        JOIN books b ON b.taken_by_student_id = s.id
                        JOIN marks m ON m.student_id = s.id
                        JOIN lessons l ON l.id = m.lesson_id
                        JOIN subjects sub ON sub.id = l.subject_id

               """)
db_data = [tuple(map(str, row)) for row in cursor.fetchall()]

missing_data = []
for row in data:
    if row not in db_data:
        missing_data.append(row)

print("Отсутствующие данные в БД:")
for row in missing_data:
    print(row)

db.close()

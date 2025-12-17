import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
    autocommit=True
)

cursor = db.cursor()
db.ping(reconnect=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ('Richardson', 'Nikola')
)
student_id = cursor.lastrowid


query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('История', student_id),
    ('Английский', student_id),
    ('Математике', student_id)
]
cursor.executemany(query, values)

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ('исследователи', 'September', 'Май')
)
group_id = cursor.lastrowid

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)


subjects = {}
for title in ('физика', 'английский', 'изо'):
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    subjects[title] = cursor.lastrowid


lessons_data = {
    'математика': 'физика',
    'физика': 'физика',
    'латынь': 'английский',
    'английский': 'английский',
    'картины': 'изо',
    'натюрморт': 'изо'
}

lessons = {}
for lesson, subject in lessons_data.items():
    cursor.execute(
        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
        (lesson, subjects[subject])
    )
    lessons[lesson] = cursor.lastrowid

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
marks = [
    (5, lessons['математика'], student_id),
    (3, lessons['физика'], student_id),
    (4, lessons['латынь'], student_id),
    (4, lessons['английский'], student_id),
    (5, lessons['картины'], student_id),
    (5, lessons['натюрморт'], student_id)
]

cursor.executemany(query, marks)

cursor.execute("""
SELECT s.name, s.second_name, m.value
FROM students s
JOIN marks m ON s.id = m.student_id
WHERE s.id = %s
""", (student_id,))
print(cursor.fetchall())

cursor.execute("""
SELECT *
FROM books
WHERE taken_by_student_id = %s
""", (student_id,))
print(cursor.fetchall())

cursor.execute("""
SELECT s.name, s.second_name, g.title, g.start_date, g.end_date, m.value, l.title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
WHERE s.id = %s
""", (student_id,))
print(cursor.fetchall())

db.close()

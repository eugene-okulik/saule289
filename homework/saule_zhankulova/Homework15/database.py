import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ('Richardson', 'Nikola')
)
student_id = cursor.lastrowid
db.commit()

books = ['История', 'Английский', 'Математика']
for book in books:
    cursor.execute(
        "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
        (book, student_id)
    )
db.commit()

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ('исследователи', 'September', 'Май')
)
group_id = cursor.lastrowid

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
db.commit()

subjects = {}
for title in ('физика', 'английский', 'изо'):
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    subjects[title] = cursor.lastrowid
db.commit()

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
db.commit()

marks = [
    (5, 'математика'),
    (3, 'физика'),
    (4, 'латынь'),
    (4, 'английский'),
    (5, 'картины'),
    (5, 'натюрморт')
]

for value, lesson in marks:
    cursor.execute(
        "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
        (value, lessons[lesson], student_id)
    )
db.commit()

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
INSERT INTO `students`  (name, second_name) VALUES  ('Samanta', 'Snorkel')

SELECT * FROM students s WHERE s.name  = 'Samanta' and s.second_name = 'Snorkel'

INSERT INTO books (title, taken_by_student_id) VALUES ('Философия', 21887)

INSERT INTO books (title, taken_by_student_id) VALUES ('Япония', 21887)

INSERT INTO books (title, taken_by_student_id) VALUES ('English', 21887)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('qa testers_new', 'September', 'January')

SELECT * FROM `groups` g WHERE g.title = 'qa testers_new'

UPDATE students s SET group_id = 21662 WHERE id = 21887

INSERT INTO subjects (title) VALUES ('philosophy')

INSERT INTO subjects (title) VALUES ('English')

INSERT INTO subjects (title) VALUES ('Japan')

INSERT INTO lessons  (title, subject_id)
VALUES
('History', 13212),
('Languages', 13211),
('Philosophy', 13210),
('History of England', 13211),
('Japan language', 13212),
('World', 13210)

SELECT * FROM lessons l ORDER BY l.id   DESC LIMIT 6

INSERT INTO marks (value, lesson_id, student_id)
VALUES
(5, 73817, 21887),
(3, 73818, 21887),
(4, 73819, 21887),
(5, 73820, 21887),
(4, 73821, 21887),
(5, 73822, 21887)


SELECT s.name, s.second_name, m.value  FROM students s JOIN  marks m ON s.id = m.student_id WHERE  s.id = 21887

SELECT *FROM books b where b.taken_by_student_id = 21887

SELECT s.name, s.second_name, s.group_id, g.title, g.start_date, g.end_date, m.value, l.title
FROM students s JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
WHERE s.id  = 21887

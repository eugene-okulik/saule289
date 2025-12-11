INSERT INTO `students`  (name, second_name, group_id) VALUES  ('Samanta', 'Snorkel', 21651)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('qa testers', 'September', 'January')

SELECT * FROM `groups` g WHERE g.title = 'qa testers'

SELECT * FROM students s WHERE s.name  = 'Samanta' and s.second_name = 'Snorkel'

INSERT INTO books (title, taken_by_student_id) VALUES ('Философия', 21877)

INSERT INTO books (title, taken_by_student_id) VALUES ('Япония', 21877)

INSERT INTO books (title, taken_by_student_id) VALUES ('English', 21877)

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
(5, 73817, 21877),
(3, 73818, 21877),
(4, 73819, 21877),
(5, 73820, 21877),
(4, 73821, 21877),
(5, 73822, 21877)


SELECT s.name, s.second_name, m.value  FROM students s JOIN  marks m ON s.id = m.student_id WHERE  s.id = 21877

SELECT * FROM books b where b.taken_by_student_id = 21877

SELECT s.name, s.second_name, s.group_id, g.title, g.start_date, g.end_date, m.value, l.title
FROM students s JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
WHERE s.id  = 21877
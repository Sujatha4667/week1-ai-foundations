CREATE TABLE students(
id INTEGER PRIMARY KEY,
name TEXT,
marks INTEGER
);

INSERT INTO students VALUES
(1,'Akash',91),
(2,'Priya',87),
(3,'Rahul',78);

SELECT * FROM students;

SELECT AVG(marks) FROM students;
DROP table if Exists Student;
DROP table if Exists Department;
Create table If Not Exists Student (student_id int,student_name varchar(45), gender varchar(6), dept_id int);
Create table If Not Exists Department (dept_id int, dept_name varchar(255));
Truncate table Student;
insert into Student (student_id, student_name, gender, dept_id) values ('1', 'Jack', 'M', '1');
insert into Student (student_id, student_name, gender, dept_id) values ('2', 'Jane', 'F', '1');
insert into Student (student_id, student_name, gender, dept_id) values ('3', 'Mark', 'M', '2');
Truncate table Department;
insert into Department (dept_id, dept_name) values ('1', 'Engineering');
insert into Department (dept_id, dept_name) values ('2', 'Science');
insert into Department (dept_id, dept_name) values ('3', 'Law');

SELECT departmentNames.dept_name, COALESCE(nonNullCounts.student_number, 0) as student_number FROM 
    (SELECT dept_name, COUNT(*) as student_number FROM 
    Department as d
    JOIN
    Student as s
    ON
    d.dept_id = s.dept_id
    GROUP BY
    dept_name) as nonNullCounts
    RIGHT JOIN
    (SELECT dept_name from Department) departmentNames
ON
nonNullCounts.dept_name = departmentNames.dept_name
ORDER BY student_number DESC, departmentNames.dept_name ASC;


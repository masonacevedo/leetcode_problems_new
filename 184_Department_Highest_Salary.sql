DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Department;


Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');

WITH all_employees AS (
    SELECT 
        Department.name as DepartmentName,
        Department.id as DepartmentID,
        Employee.name as EmployeeName, 
        Employee.salary as EmployeeSalary
    FROM
        Employee
    JOIN
        Department
    ON
        Employee.departmentId = Department.id
), 
max_salaries as (
    SELECT 
        Department.id as DepartmentID, 
        MAX(Employee.salary) as maxSalary
    FROM
        Employee
    JOIN
        Department
    ON
        Employee.departmentId = Department.id
    GROUP BY
        Department.id

)
SELECT 
    all_employees.DepartmentName as Department,
    all_employees.EmployeeName as Employee,
    all_employees.EmployeeSalary as Salary
FROM 
    all_employees 
JOIN 
    max_salaries
ON
    all_employees.DepartmentID = max_salaries.DepartmentID
WHERE 
    max_salaries.maxSalary = all_employees.EmployeeSalary;

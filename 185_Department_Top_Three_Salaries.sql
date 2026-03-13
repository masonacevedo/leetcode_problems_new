DROP TABLE If Exists Employee;
DROP TABLE If Exists Department;

Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');


-- WITH all_employees AS (
--     SELECT 
--         Department.name as DepartmentName,
--         Department.id as DepartmentID,
--         Employee.name as EmployeeName, 
--         Employee.salary as EmployeeSalary
--     FROM
--         Employee
--     JOIN
--         Department
--     ON
--         Employee.departmentId = Department.id
-- ), 
-- max_salaries as (
--     SELECT 
--         Department.id as DepartmentID, 
--         MAX(Employee.salary) as maxSalary
--     FROM
--         Employee
--     JOIN
--         Department
--     ON
--         Employee.departmentId = Department.id
--     GROUP BY
--         Department.id

-- )
-- SELECT 
--     all_employees.DepartmentName as Department,
--     all_employees.EmployeeName as Employee,
--     all_employees.EmployeeSalary as Salary
-- FROM 
--     all_employees 
-- JOIN 
--     max_salaries
-- ON
--     all_employees.DepartmentID = max_salaries.DepartmentID
-- WHERE 
--     max_salaries.maxSalary = all_employees.EmployeeSalary;


SELECT
    Department.name as Department,
    Employee.name as Employee,
    Employee.salary as Salary
FROM
    Employee
JOIN
    Department
ON
    Employee.departmentId = Department.id
WHERE
    (Department.name, Employee.salary) IN (

        WITH allSalaries AS (
            SELECT DISTINCT
                Department.name as DepartmentName,
                Employee.salary as EmployeeSalary
            FROM 
                Employee
            JOIN
                Department
            ON
                Employee.departmentId = Department.id
        ),
        rankedSalaries AS (
            SELECT 
                allSalaries.DepartmentName as DepartmentName,
                allSalaries.EmployeeSalary as EmployeeSalary,
                ROW_NUMBER() OVER (
                    PARTITION BY 
                        allSalaries.DepartmentName 
                    ORDER BY 
                        allSalaries.EmployeeSalary DESC)
                AS salaryRank
            FROM 
                allSalaries
        )
        SELECT DepartmentName, EmployeeSalary
        FROM 
            rankedSalaries
        WHERE
            salaryRank in (1,2,3)

    );
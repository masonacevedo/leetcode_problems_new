DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (id INTEGER PRIMARY KEY AUTO_INCREMENT, salary INTEGER);

INSERT INTO Employee (salary) VALUES (200);
INSERT INTO Employee (salary) VALUES (100);
INSERT INTO Employee (salary) VALUES (300);
INSERT INTO Employee (salary) VALUES (600);
INSERT INTO Employee (salary) VALUES (300);
INSERT INTO Employee (salary) VALUES (400);
INSERT INTO Employee (salary) VALUES (300);


-- SELECT salary FROM Employee
-- ORDER BY
-- salary DESC
-- LIMIT 1
-- OFFSET 0;

DROP FUNCTION IF EXISTS getNthHighestSalary;
DELIMITER $$
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
READS SQL DATA
BEGIN
    DECLARE offset_val INTEGER;
    SET offset_val = N-1;
    RETURN (
        --   # Write your MySQL query statement below.
        SELECT DISTINCT salary FROM Employee
        ORDER BY
        salary DESC
        LIMIT 1
        OFFSET offset_val
    );
END $$

DELIMITER ;

SELECT getNthHighestSalary(10);
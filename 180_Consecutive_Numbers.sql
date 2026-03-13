DROP TABLE IF EXISTS Logs;
CREATE TABLE Logs (id INTEGER PRIMARY KEY AUTO_INCREMENT, num VARCHAR(255));

INSERT INTO Logs (num) VALUES (1);
INSERT INTO Logs (num) VALUES (1);
INSERT INTO Logs (num) VALUES (1);
INSERT INTO Logs (num) VALUES (2);
INSERT INTO Logs (num) VALUES (1);
INSERT INTO Logs (num) VALUES (2);
INSERT INTO Logs (num) VALUES (2);

WITH repeatNums as (
SELECT 
    l1.id as finalId,
    l1.num as finalValue
FROM 
    Logs as l1
JOIN
    Logs as l2
JOIN
    Logs as l3
ON
    (l1.id + 1) = l2.id
AND 
    (l1.id + 2) = l3.id
AND 
    (l1.num) = l2.num
AND
    (l2.num) = l3.num)
SELECT DISTINCT finalValue as ConsecutiveNums from repeatNums;
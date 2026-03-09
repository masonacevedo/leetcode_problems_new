DROP TABLE IF EXISTS Person;
CREATE TABLE Person (id INTEGER PRIMARY KEY AUTO_INCREMENT, email VARCHAR(255));
INSERT INTO Person (email) VALUES ("john@example.com");
INSERT INTO Person (email) VALUES ("bob@example.com");
INSERT INTO Person (email) VALUES ("john@example.com");

DELETE FROM Person 
WHERE id NOT IN
    (
        SELECT * 
        FROM (
            SELECT MIN(id) FROM Person
            GROUP BY email
        ) as temp
    );

SELECT * FROM Person;
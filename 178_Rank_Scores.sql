DROP TABLE IF EXISTS Scores;
CREATE TABLE Scores (id INTEGER PRIMARY KEY AUTO_INCREMENT, score DECIMAL(10,2));

INSERT INTO Scores (score) VALUES (3.50);
INSERT INTO Scores (score) VALUES (3.65);
INSERT INTO Scores (score) VALUES (4.00);
INSERT INTO Scores (score) VALUES (3.85);
INSERT INTO Scores (score) VALUES (4.00);
INSERT INTO Scores (score) VALUES (3.65);


SELECT s1.id, s1.score, COUNT(*)
FROM Scores as s1 JOIN 
(SELECT DISTINCT score FROM Scores ) 
as s2
WHERE 
s1.score <= s2.score
GROUP BY
s1.id, s1.score
ORDER BY 
s1.score DESC;
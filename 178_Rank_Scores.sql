DROP TABLE IF EXISTS Scores;
CREATE TABLE Scores (id INTEGER PRIMARY KEY AUTO_INCREMENT, score DECIMAL(10,2));

INSERT INTO Scores (score) VALUES (3.50);
INSERT INTO Scores (score) VALUES (3.65);
INSERT INTO Scores (score) VALUES (4.00);
INSERT INTO Scores (score) VALUES (3.85);
INSERT INTO Scores (score) VALUES (4.00);
INSERT INTO Scores (score) VALUES (3.65);

SELECT original.score, rankedTable.rank
FROM
Scores as original JOIN
(SELECT score, ROW_NUMBER() OVER (ORDER BY score DESC) as "rank" FROM (
    SELECT DISTINCT score FROM Scores ORDER BY score DESC
) as ranked) as rankedTable
ON
original.score = rankedTable.score
ORDER BY
rankedTable.rank ASC;
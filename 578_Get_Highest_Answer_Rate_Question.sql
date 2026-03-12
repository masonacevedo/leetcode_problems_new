Create table If Not Exists SurveyLog (id int, action varchar(255), question_id int, answer_id int, q_num int, timestamp int);
Truncate table SurveyLog;
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '285', NULL, '1', '123');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'answer', '285', '124124', '1', '124');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '369', NULL, '2', '125');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'skip', '369', NULL, '2', '126');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('6', 'show', '369', NULL, '2', '127');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('6', 'answer', '369', '574803', '2', '128');


SELECT * FROM
(SELECT showTable.question_id AS qid, answerCount/showCount as answerRate FROM
    (SELECT question_id, action, COUNT(*) as showCount FROM SurveyLog
    GROUP BY 
    question_id, action
    HAVING action="show") as showTable
    JOIN
    (SELECT question_id, action, COUNT(*) as answerCount FROM SurveyLog
    GROUP BY 
    question_id, action
    HAVING action="answer") as answerTable
    ON
    showTable.question_id=answerTable.question_id) as rateTable
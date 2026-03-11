Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

SELECT ROUND(numerator/denominator,2) as fraction FROM 
(SELECT COUNT(*) as numerator FROM (
    SELECT DISTINCT a1.player_id 
    FROM Activity as a1
    JOIN Activity as a2
    ON
    (DATE_ADD(a1.event_date, INTERVAL 1 DAY) = a2.event_date 
    AND a1.player_id = a2.player_id
    AND a1.event_date = (SELECT MIN(event_date) FROM Activity WHERE player_id=a1.player_id))
) as temp) as numeratorTable
JOIN 
    (SELECT COUNT(*) AS denominator FROM 
        (SELECT DISTINCT player_id 
        FROM Activity) 
    AS allPlayersTable) 
    AS denominatorTable;

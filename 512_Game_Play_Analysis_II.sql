DROP TABLE IF EXISTS Activity;
CREATE TABLE Activity (
    player_id INTEGER, 
    device_id INTEGER, 
    event_date DATE, 
    games_played INT, 
    PRIMARY KEY (player_id, event_date)
);

insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

select player_id, MIN(event_date) as first_login from Activity
GROUP BY player_id;
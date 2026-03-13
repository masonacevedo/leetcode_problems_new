DROP TABLE IF EXISTS Insurance;
Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float);
Truncate table Insurance;
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40');

-- select * from Insurance
-- WHERE
-- tiv_2015 in ;

SELECT ROUND(sum(tiv_2016), 2) as tiv_2016 FROM Insurance
WHERE
tiv_2015 IN (
        SELECT tiv_2015 FROM (
            SELECT tiv_2015, count(*) as numWithAmount
            FROM Insurance
            GROUP BY tiv_2015
            HAVING numWithAmount > 1) as temp
        )
AND
(lat, lon) IN (
    SELECT lat, lon
    FROM (
        SELECT lat, lon, count(*) as locCount
        FROM Insurance
        GROUP BY lat, lon
        HAVING locCount = 1
        ) as temp
    );
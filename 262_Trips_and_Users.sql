DROP TABLE IF EXISTS Trips;
DROP TABLE IF EXISTS Users;
Create table If Not Exists Trips (id int, client_id int, driver_id int, city_id int, status ENUM('completed', 'cancelled_by_driver', 'cancelled_by_client'), request_at varchar(50));
Create table If Not Exists Users (users_id int, banned varchar(50), role ENUM('client', 'driver', 'partner'));
Truncate table Trips;
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('1', '1', '10', '1', 'completed', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('3', '3', '12', '6', 'completed', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('5', '1', '10', '1', 'completed', '2013-10-02');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('6', '2', '11', '6', 'completed', '2013-10-02');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('7', '3', '12', '6', 'completed', '2013-10-02');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('8', '2', '12', '12', 'completed', '2013-10-03');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('9', '3', '10', '12', 'completed', '2013-10-03');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03');
Truncate table Users;
insert into Users (users_id, banned, role) values ('1', 'No', 'client');
insert into Users (users_id, banned, role) values ('2', 'Yes', 'client');
insert into Users (users_id, banned, role) values ('3', 'No', 'client');
insert into Users (users_id, banned, role) values ('4', 'No', 'client');
insert into Users (users_id, banned, role) values ('10', 'No', 'driver');
insert into Users (users_id, banned, role) values ('11', 'No', 'driver');
insert into Users (users_id, banned, role) values ('12', 'No', 'driver');
insert into Users (users_id, banned, role) values ('13', 'No', 'driver');


-- Trips that were cancelled by someone not banned
WITH bannedIds AS 
    (
        SELECT users_id FROM Users WHERE banned="Yes"
    ), 
cancelledTrips AS 
    (SELECT DISTINCT 
        Trips.id AS tripID,
        Trips.request_at AS requestDate
    FROM
        Trips
    WHERE
        request_at >= "2013-10-01" AND request_at <= "2013-10-03"
        AND (
            status = "cancelled_by_driver" OR status = "cancelled_by_client")
        AND (
            Trips.client_id NOT IN (SELECT users_id FROM bannedIds)
        )
    ), 
-- All trips between requested dates
allTrips AS (
    SELECT DISTINCT 
        -- Trips.id AS tripID
        -- Trips.request_at AS requestDate
        Trips.id as tripId,
        Trips.request_at as request_at
        -- *
    FROM
        Trips
    WHERE
        trips.client_id NOT IN (
            SELECT 
                users_id 
            FROM 
                Users
            WHERE 
                banned = "Yes"
        )
        AND
        trips.driver_id NOT IN (
            SELECT 
                users_id 
            FROM 
                Users
            WHERE 
                banned = "Yes"
        )
    ),
-- number of cancelled trips on each day
cancellationsByDate AS ( 
    SELECT DISTINCT
        requestDate, 
        COUNT(*) OVER (PARTITION BY requestDate) as cancellationCount
    FROM 
        cancelledTrips),
-- number of trips on each day
tripsByDate AS (
    SELECT
        request_at,
        COUNT(tripId) as tripCount
    FROM
        allTrips
    GROUP BY 
        request_at
)
-- cancellation rate!
SELECT 
    tripsByDate.request_at as Day,
    cancellationCount, 
    tripCount,
    COALESCE(cancellationCount/tripCount, 0) as "Cancellation Rate"
FROM 
    tripsByDate
LEFT JOIN
    cancellationsByDate
ON
    tripsByDate.request_at = cancellationsByDate.requestDate;
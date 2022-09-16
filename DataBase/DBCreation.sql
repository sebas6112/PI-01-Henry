USE `pi-01`;

SET GLOBAL log_bin_trust_function_creators = 1;

CREATE TABLE IF NOT EXISTS drivers(
driverId 		INTEGER,
driverRef 		VARCHAR(255),
number 			VARCHAR(255),
code 			VARCHAR(4),
forename 		VARCHAR(255),
surname 		VARCHAR(255),
dob 			DATE,
nationality 	VARCHAR(255),
url 			VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\drivers.csv' 
INTO TABLE drivers
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS constructors(
constructorId 		INTEGER,
constructorRef 		VARCHAR(255),
name 				VARCHAR(255),
nationality 		VARCHAR(255),
url			 		VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\constructors.csv' 
INTO TABLE constructors
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS circuits(
circuitId 		INTEGER,
circuitRef 		VARCHAR(255),
name 			VARCHAR(255),
location 		VARCHAR(255),
country			VARCHAR(255),
lat 			FLOAT,
lng 			FLOAT,
alt 			INTEGER,
url			 	VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\circuits.csv' 
INTO TABLE circuits
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS races(
raceId	 		INTEGER,
year 			INTEGER,
round 			INTEGER,
circuitId 		INTEGER,
name 			VARCHAR(255),
date 			DATE,
time 			VARCHAR(255),
url				VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\races.csv' 
INTO TABLE races
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS qualifying(
qualifyId	 		INTEGER,
raceId 				INTEGER,
driverId 			INTEGER,
constructorId 		INTEGER,
number 				INTEGER,
position 			INTEGER,
q1 					VARCHAR(255),
q2 					VARCHAR(255),
q3					VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\qualifying.csv' 
INTO TABLE qualifying
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS results(
resultId	 		INTEGER,
raceId 				INTEGER,
driverId 			INTEGER,
constructorId 		INTEGER,
number 				VARCHAR(255),
grid 				INTEGER,
position 			VARCHAR(255),
positionText		VARCHAR(255),
positionOrder		INTEGER,
points	 			FLOAT,
lap 				INTEGER,
time 				VARCHAR(255),
milliseconds 		VARCHAR(255),
fastestLap 			VARCHAR(255),
`rank` 				VARCHAR(255),
fastestLapTime 		VARCHAR(255),
fastestLapSpeed 	VARCHAR(255),
statusId			INTEGER
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\results.csv' 
INTO TABLE results
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS pitStops(
raceId	 		INTEGER,
driverId 		INTEGER,
stop 			INTEGER,
lap 			INTEGER,
time 			TIME,
duration 		VARCHAR(255),
milliseconds 	INTEGER
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\pitStops.csv' 
INTO TABLE pitStops
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE IF NOT EXISTS lapTimes(
raceId	 		INTEGER,
driverId 		INTEGER,
lap 			INTEGER,
position 		INTEGER,
time 			VARCHAR(255),
milliseconds 	INTEGER
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\NData\\lapTimes.csv' 
INTO TABLE lapTimes
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;
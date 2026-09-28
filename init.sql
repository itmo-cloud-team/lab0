ALTER USER 'mysql'@'localhost' IDENTIFIED BY '1';

CREATE DATABASE IF NOT EXISTS aircraft CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
GRANT ALL PRIVILEGES ON aircraft.* TO 'mysql'@'localhost';
FLUSH PRIVILEGES;

USE aircraft;
CREATE TABLE IF NOT EXISTS aircraft(
    tail_number VARCHAR(10) NOT NULL,
    production_date TIMESTAMP NOT NULL,
    icao_aircraft_type VARCHAR(6) NOT NULL,
    PRIMARY KEY (tail_number)
);

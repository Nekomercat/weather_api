CREATE DATABASE deal_engine;

CREATE TABLE travel_tickets (
    origin character varying(3), 
    destination character varying(3), 
    airline character varying(2), 
    flight_num integer NOT NULL, 
    origin_iata_code character varying(3), 
    origin_name character varying(100), 
    origin_latitud double precision, 
    origin_longitud double precision, 
    destination_iata_code character varying(3), 
    destination_name character varying(100), 
    destination_latitud double precision, 
    destination_longitud double precision
);

COPY travel_tickets FROM '/app/challenge_dataset.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE travel_tickets ADD COLUMN id SERIAL PRIMARY KEY;
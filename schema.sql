CREATE TABLE IF NOT EXISTS travel_tickets (
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

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 
        FROM information_schema.tables 
        WHERE table_name = 'travel_tickets'
    ) THEN
        IF (SELECT count(*) FROM travel_tickets) = 0 THEN
            COPY travel_tickets FROM '/app/challenge_dataset.csv' DELIMITER ',' CSV HEADER;
            ALTER TABLE travel_tickets ADD COLUMN id SERIAL PRIMARY KEY;
        ELSE
            RAISE NOTICE 'La tabla existe pero no está vacía';
        END IF;
    ELSE
        RAISE NOTICE 'La tabla no existe';
    END IF;
END $$;
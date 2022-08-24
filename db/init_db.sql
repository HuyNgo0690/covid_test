CREATE TABLE IF NOT EXISTS country
(
    country_id serial NOT NULL,
    country_name character(200) NOT NULL,
    region_id bigint,
    confirmed bigint NOT NULL,
    recovered bigint NOT NULL,
    deaths bigint NOT NULL,
    population bigint NOT NULL,
    sq_km_area bigint NOT NULL,
    life_expectancy character(20) NOT NULL,
    elevation_in_meters character(200) NOT NULL,
    continent character(100) NOT NULL,
    abbreviation character(50) NOT NULL,
    location character(200) NOT NULL,
    iso character(50) NOT NULL,
    capital_city character(200) NOT NULL,
    lat character(200) NOT NULL,
    "long" character(200) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (country_id)
);

CREATE TABLE IF NOT EXISTS region (
    region_id serial NOT NULL,
    country_id bigint NOT NULL,
    region_name character(200) NOT NULL,
    lat numeric NOT NULL,
    "long" numeric NOT NULL,
    confirmed bigint NOT NULL,
    recovered bigint NOT NULL,
    deaths bigint NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (region_id),
    FOREIGN KEY (country_id) REFERENCES country(country_id) 
);
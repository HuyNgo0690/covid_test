CREATE TABLE covid.country
(
    country_id serial NOT NULL,
    country_name character(200) NOT NULL,
    confirmed bigint NOT NULL,
    recovered bigint NOT NULL,
    deaths bigint NOT NULL,
    country_population bigint NOT NULL,
    sq_km_area bigint NOT NULL,
    life_expectancy numeric NOT NULL,
    elevation_in_meters numeric NOT NULL,
    continent character(20) NOT NULL,
    abbreviation character(10) NOT NULL,
    location character(200) NOT NULL,
    iso smallint NOT NULL,
    capital_city character(200) NOT NULL,
    lat numeric NOT NULL,
    "long" numeric NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
    CONSTRAINT country_pk PRIMARY KEY (country_id)
);


);

CREATE TABLE covid.region (
    region_id serial NOT NULL,
    country_id bigint NOT NULL,
    region_name character(200) NOT NULL,
    lat numeric NOT NULL,
    "long" numeric NOT NULL,
    confirmed bigint NOT NULL,
    recovered bigint NOT NULL,
    deaths bigint NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
    CONSTRAINT region_pk PRIMARY KEY (region_id),
    CONSTRAINT region_fk FOREIGN KEY (region_id)
        REFERENCES public.country (country_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);
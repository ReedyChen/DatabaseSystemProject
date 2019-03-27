DROP TABLE IF EXISTS hospital;
DROP TABLE IF EXISTS measurement;
DROP TABLE IF EXISTS state;
DROP TABLE IF EXISTS death;


CREATE TABLE hospital(
	name VARCHAR(255),
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zipcode INTEGER,
	phone VARCHAR(11),
	county_name VARCHAR(255),
 	PRIMARY KEY (name)
);

CREATE TABLE measurement(
	hospital_name VARCHAR(255),
	address VARCHAR(255),
	measure_name VARCHAR(255),
	measure_id VARCHAR(255),
	denominator INTEGER,
	score FLOAT,
	lower_estimate FLOAT,
	higher_estimate FLOAT,
	start_year INTEGER,
	end_year INTEGER,
	PRIMARY KEY (measure_name, hospital_name)
);

CREATE TABLE state(
	name VARCHAR(255),
	measure_name VARCHAR(255),
	num_of_hosp_worse INTEGER,
	num_of_hosp_same INTEGER,
	num_of_hosp_better INTEGER,
	PRIMARY KEY (name, measure_name)
);

CREATE TABLE death(
	cause_name  VARCHAR(255),
	year INTEGER,
	deaths INTEGER,
	age_adjusted_death_rate FLOAT,
	state_name VARCHAR(255)

);

# DatabaseSystemProject

## Objective

The objective of this project is to find the relationship between the hospital rating and the death rate of multiple types of diseases within the same area. By using the attributes these two data sets shared — city, state, and zip code, we can calculate the multiplier of rating and death rate of each disease. Thus, we could find out which disease is closely related to hospital quality and which are not. The result could be used for the patient to choose which hospital is most suitable for his/her treatment or recovery.

## Building and Running

1. Install python config using `pip install config`.
2. Install python psycopg2 using `pip install psycopg2`.
3. Run `psql` in terminal.
    - create database called 'hospital' using `CREATE DATABASE hospital;`.
        (In this case, using hospital as the database name)
4. Run schema.sql in the database 'hospital'. 
    - go to the database `hospital`.
    - run `\i /.../schema.sql` to create data schema.
5. Run `python load_data.py` in terminal. 	

## Data
1. Hospital General Information.csv
2. Complications and Deaths - Hospital.csv
3. Complications and Deaths - State.csv
4. NCHS_-_Leading_Causes_of_Death__United_States.csv

## Notice
Any data which is not avalible in the database is assigend with value of -1.

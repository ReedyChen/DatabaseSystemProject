# DatabaseSystemProject

## Objective

The objective of this project is to find the relationship between the hospital rating and the death rate of multiple types of diseases within the same area. By using the attributes these two data sets shared — city, state, and zip code, we can calculate the multiplier of rating and death rate of each disease. Thus, we could find out which disease are closely related to hospital quality and which are not. The result could be used for the patient to choose which hospital is most suitable for his/her treatment or recovery.

## Data files
1. Hospital General Information.csv
2. Complications and Deaths - Hospital.csv
3. Complications and Deaths - State.csv
4. NCHS_-_Leading_Causes_of_Death__United_States.csv

## Loading Data
1. Install config using `pip install config`.
2. Install psycopg2 using `pip install psycopg2`.
3. Run `psql` in terminal.
    - create database called 'hospital' using `CREATE DATABASE hospital;`.
        (In this case, we are using hospital as the database name)
4. Quit current database, run  `psql hospital` in your terminal to enter databse `hospital`
    Run schema.sql in the database 'hospital'. 
    - go to the database `hospital`.
    - run `\i /.../schema.sql` to create data schema.
5. Run `python load_data.py` in terminal to load all the data. 	

## Running application
1. Install tabulate using `pip install tabulate`.
2. Install flask using `pip install flask`.
3. At the file directory, run `export FLASK_APP=web.py`
4. Then run `Flask run`, and open `http://127.0.0.1:5000` in your web browser, this should open the app

## Notice
Any data which is not avalible in the database is assigend with value of -1.

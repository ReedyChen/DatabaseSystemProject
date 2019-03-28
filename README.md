# DatabaseSystemProject

## Objective

The objective of this project is to find the relationship between the hospital rating and the death rate of multiple types of diseases within the same area. By using the attributes these two data sets shared — city, state, and zip code, we can calculate the multiplier of rating and death rate of each disease. Thus, we could find out which disease is closely related to hospital quality and which are not. The result could be used for the patient to choose which hospital is most suitable for his/her treatment or recovery.

## Building and Running

1. Install python config using `pip install config`
2. Create your own database named as whatever you want. 
- run `psql` in terminal
- create database using `CREATE DATABASE hospital;` (In this case, using hospital as the database name)
3. Change the database_name variable to your database name. (line 268)
- database_name = "hospital"
4. Run schema.sql in the database. 
- go to the database `hospital`
- run `\i /.../schema.sql`
5. Quit psql and Run `python load_data.py` in terminal. 	
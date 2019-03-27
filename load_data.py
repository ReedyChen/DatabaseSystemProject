import csv
import psycopg2
import config

# hospital table insert
def hospitalInsert(myDBname):
    try:
        connection = psycopg2.connect(dbname = myDBname)
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO hospital (name, address, city, state, zipcode, county_name) VALUES (%s,%s,%s,%s,%s,%s)"""
        for i in range(len(name)):
            try:
                record_to_insert = (name[i], address1[i], city[i], state[i], ZIP[i], county[i])
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
            except(Exception, psycopg2.Error) as error:
                print(error)
                connection.rollback()
        count = cursor.rowcount
        print (count, "Record inserted successfully into hospital table")
    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into hospital table", error)
    connection.close()
    
# measurement table insert
def measurementInsert(myDBname):
    try:
        connection = psycopg2.connect(dbname = myDBname)
        cursor = connection.cursor()
        
        # measurement insert 
        print(len(hosp_name))
        postgres_insert_query = """ INSERT INTO measurement (hospital_name, address, measure_name, measure_id, denominator, score, lower_estimate, higher_estimate, start_year, end_year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        for i in range(len(hosp_name)):
            
            try:
                record_to_insert = (hosp_name[i], address2[i], measure_name[i], measure_id[i], denominator[i], score[i], le[i], he[i], sy[i], ey[i])
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
            except(Exception, psycopg2.Error) as error:
                print(error)
                connection.rollback()
        count = cursor.rowcount
        print (count, "Record inserted successfully into measurement table")
    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into measurement table", error)
    connection.close()
  
# state table insert      
def stateInsert(myDBname):
    try:
        connection = psycopg2.connect(dbname = myDBname)
        cursor = connection.cursor()
        
        # measurement insert 
        print(len(state_name))
        postgres_insert_query = """ INSERT INTO state (name, measure_name, num_of_hosp_worse, num_of_hosp_same, num_of_hosp_better) VALUES (%s,%s,%s,%s,%s)"""
        for i in range(len(state_name)):
            
            try:
                record_to_insert = (state_name[i], mea _name[i], num_worse[i], num_same[i], num_better[i])
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
            except(Exception, psycopg2.Error) as error:
                print(error)
                connection.rollback()
        count = cursor.rowcount
        print (count, "Record inserted successfully into state table")
    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into state table", error)
    connection.close()
   
# death table insert      
def deathInsert(myDBname):
        try:
        connection = psycopg2.connect(dbname = myDBname)
        cursor = connection.cursor()
        
        # measurement insert 
        print(len(cause_name))
        postgres_insert_query = """ INSERT INTO death (cause_name, year, deaths, age_adjusted_death_rate, state_name) VALUES (%s,%s,%s,%s,%s)"""
        for i in range(len(state_name)):
            
            try:
                record_to_insert = (cause_name[i], year[i], deaths[i], age_adj_death_rate[i], state_name[i])
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
            except(Exception, psycopg2.Error) as error:
                print(error)
                connection.rollback()
        count = cursor.rowcount
        print (count, "Record inserted successfully into death table")
    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into death table", error)
    connection.close()    
    
    
with open('Hospital General Information.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    name, address1, city, state, ZIP, county = [], [], [], [], [], []
    for row in csv_reader:
        if line_count == 0:
            for i in range(len(row)):
                if (row[i] == "Hospital Name"):
                    nameID = i
                elif (row[i] == "Address"):
                    addressID = i
                elif (row[i] == "City"):
                    cityID = i
                elif (row[i] == "State"):
                    stateID = i
                elif (row[i] == "ZIP Code"):
                    ZIPID = i
                elif (row[i] == "County Name"):
                    countyID = i
        else:
            for i in range(len(row)):
                if (i == nameID):
                    name.append(row[i])
                elif (i == addressID):
                    address1.append(row[i])  
                elif (i == cityID):
                    city.append(row[i])   
                elif (i == stateID):
                    state.append(row[i])   
                elif (i == ZIPID):
                    ZIP.append(row[i])  
                elif (i == countyID):
                    county.append(row[i])                  
        line_count += 1

with open('Complications and Deaths - Hospital.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    hosp_name, address2, measure_name, measure_id, denominator, score, le, he, sy, ey= [], [], [], [], [], [], [], [], [], []
    for row in csv_reader:        
        if line_count == 0:
            for i in range(len(row)):
                if (row[i] == "Hospital Name"):
                    n1 = i
                elif (row[i] == "Address"):
                    n2 = i
                elif (row[i] == "Measure Name"):
                    n3 = i
                elif (row[i] == "Measure ID"):
                    n4 = i
                elif (row[i] == "Denominator"):
                    n5 = i
                elif (row[i] == "Score"):
                    n6 = i
                elif (row[i] == "Lower Estimate"):
                    n7 = i
                elif (row[i] == "Higher Estimate"):
                    n8 = i  
                elif (row[i] == "Measure Start Date"):
                    n9 = i
                elif (row[i] == "Measure End Date"):
                    n10 = i       
        else:
            
            for i in range(len(row)):
                if (row[i] == "Not Available"):
                    row[i] = -1
                if (i == n1):                    
                    hosp_name.append(row[i])      
                elif (i == n2):
                    address2.append(row[i])    
                elif (i == n3):
                    measure_name.append(row[i])    
                elif (i == n4):
                    measure_id.append(row[i])    
                elif (i == n5):
                    denominator.append(row[i])    
                elif (i == n6):
                    score.append(row[i])    
                elif (i == n7):
                    le.append(row[i])    
                elif (i == n8):
                    he.append(row[i])    
                elif (i == n9):
                    s_year = row[i].split('/')[-1]
                    sy.append(s_year)    
                elif (i == n10):
                    e_year = row[i].split('/')[-1]
                    ey.append(e_year)                    
        
        line_count += 1
		
with open('Complications and Deaths - State.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    state_name, mea_name, num_worse, num_same, num_better= [], [], [], [], []
    for row in csv_reader:        
        if line_count == 0:
            for i in range(len(row)):
                if (row[i] == "State"):
                    n1 = i
                elif (row[i] == "Measure Name"):
                    n2 = i
                elif (row[i] == "Number of Hospitals Worse"):
                    n3 = i
                elif (row[i] == "Number of Hospitals Same"):
                    n4 = i
                elif (row[i] == "Number of Hospitals Better"):
                    n5 = i    
        else:
            
            for i in range(len(row)):
                if (i == n1):                    
                    state_name.append(row[i])      
                elif (i == n2):
                    mea_name.append(row[i])    
                elif (i == n3):
                    num_worse.append(row[i])    
                elif (i == n4):
                    num_same.append(row[i])    
                elif (i == n5):
                    num_better.append(row[i])                       
        
        line_count += 1
		
with open('NCHS_-_Leading_Causes_of_Death__United_States.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    cause_name, year, deaths, age_adj_death_rate, state_name= [], [], [], [], []
    for row in csv_reader:        
        if line_count == 0:
            for i in range(len(row)):
                if (row[i] == "Cause Name"):
                    n1 = i
                elif (row[i] == "Year"):
                    n2 = i
                elif (row[i] == "Deaths"):
                    n3 = i
                elif (row[i] == "Age-adjusted Death Rate"):
                    n4 = i
                elif (row[i] == "State"):
                    n5 = i    
        else:
            
            for i in range(len(row)):
                if (i == n1):                    
                    cause_name.append(row[i])      
                elif (i == n2):
                    year.append(row[i])    
                elif (i == n3):
                    deaths.append(row[i])    
                elif (i == n4):
                    age_adj_death_rate.append(row[i])    
                elif (i == n5):
                    state_name.append(row[i])                       
        
        line_count += 1


# *** create your own database named as whatever you want ***
# *** then run the query "schema.sql" in your data base ***

database_name = "www" # change the var name to your database name
hospitalInsert(database_name)
measurementInsert(database_name)
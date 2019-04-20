from flask import Flask, render_template, Response, request
import psycopg2
from tabulate import tabulate

app = Flask(__name__)

conn_string = "host='localhost' dbname='hospital'"

conn = psycopg2.connect(conn_string)
# cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()


def select_from_state(state):
    # query = "SELECT * FROM course WHERE semester='" + semester + "'"
    query = "SELECT * FROM hospital WHERE state='%s'" % state
    cursor.execute(query, [state])
    records = cursor.fetchall()
    return records


def insert(name, semester):
    query = "INSERT INTO course(name, semester) VALUES('" + name + "', '" + semester + "')"
    cursor.execute(query)
    conn.commit()
	
#given cause and year, select top 10 states that have the lowest death rate ---return:(state_name, deathrate)
def death_rate_rank(cause,year):
    cursor.execute("SELECT state_name,age_adjusted_death_rate FROM death WHERE year = %s AND cause_name =%s ORDER BY age_adjusted_death_rate LIMIT 10", (year,cause_name))
    records = cursor.fetchall()
    return records

# select top 10 hospitals given state and measure name based on their scores ---return:(hospital_name, score)
def top_hospital_state(state,measurement):
    cursor.execute("SELECT hospital_name,score FROM measurement,hospital WHERE hospital_name = name AND state = %s AND measure_name = %s ORDER BY score DESC LIMIT 10", (state,measurement))
    records = cursor.fetchall()
    return records   

# select top 10 hospitals (overall) based on the avrage score ---(hospital_name, average_score)
def best_ten():
    cursor.execute("SELECT hospital_name,AVG(score) FROM measurement GROUP BY hospital_name ORDER BY AVG(score) DESC LIMIT 10")
    records = cursor.fetchall()
    return records

# select top 10 hospitals given a state (in that state) based on avrage score ---return:(hospital_name, average_score)
def best_ten_state(state):
    cursor.execute("SELECT hospital_name,AVG(score) FROM measurement,hospital WHERE hospital_name = name AND state=%s GROUP BY hospital_name ORDER BY AVG(score) DESC LIMIT 10",(state,))
    records = cursor.fetchall()
    return records   

#def death_rate_rank_hospital(cause,year):
    #cursor.execute("SELECT state_name,age_adjusted_death_rate FROM death WHERE year = %s AND cause_name =%s ORDER BY age_adjusted_death_rate LIMIT 1", (year,cause_name))
    #records = cursor.fetchall()
    #return records
	
# given state and city, return all the hopstial in that city with informations ---return:(name, address, phone, zipcode)
def hospital_info(s,c):
    cursor.execute("SELECT name, address, phone, zipcode FROM hospital WHERE state=s AND city=c")
    records = cursor.fetchall()
    return records
	
# No.1 hospital based on measurement score (average) and death rate (deathrate first then avescore) ---return: (hospital_name, death_rate, average_score)
def top_one_hospital():
    cursor.execute("SELECT hospital_name, age_adjusted_death_rate, avescore FROM death, (SELECT hospital_name,AVG(score) AS avescore,state FROM measurement,hospital WHERE hospital_name = name GROUP BY hospital_name, state ORDER BY AVG(score) DESC) WHERE state=state_name ORDER BY age_adjusted_death_rate, avescore DESC")


@app.route('/')
def index():
    conn.rollback()
    return render_template('index.html')


@app.route("/select_from_state", methods=['GET','POST'])
def search():
    records = select_from_state(request.form['state'])
    return Response(
        tabulate(records),
        mimetype="text/plain"
    )


@app.route("/new-course", methods=['POST'])
def new_course():
    insert(request.form['course-name'], request.form['semester'])
    cursor.execute("SELECT * FROM course")
    records = cursor.fetchall()
    return Response(
        tabulate(records),
        mimetype="text/plain"
    )

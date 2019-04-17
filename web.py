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

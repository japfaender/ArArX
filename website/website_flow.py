from flask import Blueprint,render_template,request,flash,redirect
import mariadb
import pandas as pd

website_flow = Blueprint("website_flow", __name__)

@website_flow.route('/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        global username, password,database
        username = request.form.get('Username')
        database = request.form.get('Database')
        password = request.form.get('Password')
        print("username: ", username,
              "database: ", database,
              " password: ", password)
        try:
            conn = mariadb.connect(
                user=username,
                password=password,
                host="139.20.22.156",
                port=3306,
                database=database)
            print("redirect")
            return redirect('/dashboard')
        except mariadb.Error as e:
            flash(
                f"Error connecting to MariaDB Platform: {e}", category='error')
    return render_template("login.html")


@website_flow.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    conn_arardb = mariadb.connect(
        user=username,
        password=password,
        host="139.20.22.156",
        port=3306,
        database=database)
    dashboard_arardb = pd.read_sql(
        "SELECT exp_nr,material,proben_bez,project_name,sample_owner,irr_batch  FROM material order by exp_nr ", conn_arardb)
    dashboard_arardb_column_names=['expr no','material','probe','project name', 'sample owner', 'irr batch']
    if request.method == 'POST':
        dashboard_arardb = pd.read_sql(
            "SELECT exp_nr,material,proben_bez,project_name,sample_owner,irr_batch  FROM material order by exp_nr ", conn_arardb)
    return render_template("dashboard.html", title=database, column_names=dashboard_arardb_column_names, row_data=list(dashboard_arardb.values.tolist()), zip=zip)


"""
                user="root",
            password="dbpwx61",
            database="arardb" 
"""
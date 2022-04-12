from flask import Blueprint,render_template,request,flash,redirect
import mariadb
import pandas as pd

website_flow = Blueprint("website_flow", __name__)

@website_flow.route('/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        global username, password
        username = request.form.get('Username')
        password = request.form.get('Password')
        print("username: ", username,
              " password: ", password)
        try:
            conn = mariadb.connect(
                user=username,
                password=password,
                host="139.20.22.156",
                port=3306,
                database="arardb")
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
        database="arardb")
    dashboard_arardb = pd.read_sql(
        "SELECT exp_nr,material,proben_bez,project_name,sample_owner,irr_batch  FROM material", conn_arardb)
    print(dashboard_arardb)
    return render_template("dashboard.html", tables=[dashboard_arardb.to_html()], titles=['List-of-experiments'])


"""
                user="root",
            password="dbpwx61",
"""
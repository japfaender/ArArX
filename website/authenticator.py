import mariadb
import sys
from flask import Blueprint, redirect, request, flash, render_template, redirect



auth = Blueprint("auth", __name__)


@auth.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        print("username: ", username,
              " password: ", password)
        try:
            global conn
            conn = mariadb.connect(
                user=username,
                password=password,
                host="139.20.22.156",
                port=3306,
                database="arardb")
            return redirect('/dashboard')
        except mariadb.Error as e:
            flash(
                f"Error connecting to MariaDB Platform: {e}", category='error')
    return render_template("home.html")


@auth.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")
"""

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="dbpwx61",
        host="139.20.22.156",
        port=3306,
        database="arardb"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


inlet_method_equil_times = pd.read_sql(
    "SELECT * FROM inlet_method_equil_times", conn)  # (cur.fetchall())
#inlet_method_equil_times = pd.read_sql("SELECT * FROM inlet_method_equil_times", cur)
print(inlet_method_equil_times)

print(inlet_method_equil_times_data)
for (method, time) in inlet_method_equil_times_data:
    print("Method ",method, " Time ",time)
"""

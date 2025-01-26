from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection function
def get_db_connection():
    conn = psycopg.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
    return conn

@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        if not username or not password or not password_confirm:
            flash("All fields are required!")
            return render_template("register.html")

        if len(username) < 8 or len(password) < 8:
            flash("Username and password must be at least 8 characters!")
            return render_template("register.html")

        if password != password_confirm:
            flash("Passwords do not match!")
            return render_template("register.html")

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO names (username, pass) VALUES (%s, %s)", (username, password))
            conn.commit()
            flash("Registration successful!")
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"Error: {e}")
        finally:
            if conn:
                conn.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM names WHERE username = %s AND pass = %s", (username, password))
            user = cur.fetchone()
            if user:
                flash("Login successful!")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid username or password!")
        except Exception as e:
            flash(f"Error: {e}")
        finally:
            if conn:
                conn.close()

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, render_template, request, redirect, session

from werkzeug.security import generate_password_hash, check_password_hash

from models import create_connection

auth = Blueprint("auth", __name__)

# REGISTER

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = create_connection()

        cursor = conn.cursor()

        try:

            cursor.execute("""

            INSERT INTO users(name,email,password)

            VALUES(?,?,?)

            """, (name, email, hashed_password))

            conn.commit()

            return redirect("/login")

        except:

            return "Email already exists!"

        finally:

            conn.close()

    return render_template("register.html")

# LOGIN

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        conn = create_connection()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT * FROM users WHERE email=?

        """, (email,))

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]

            session["user_name"] = user["name"]

            return redirect("/dashboard")

        else:

            return "Invalid Email or Password"

    return render_template("login.html")

# LOGOUT

@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/")
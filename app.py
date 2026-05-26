from flask import Flask, render_template, request, jsonify, session, redirect

from auth import auth

from models import create_tables, create_connection

from chatbot import generate_ai_response

app = Flask(__name__)

app.secret_key = "enterprise_secret_key"

# CREATE DATABASE TABLES

create_tables()

# REGISTER AUTH ROUTES

app.register_blueprint(auth)

# HOME PAGE

@app.route("/")
def home():

    return render_template("index.html")

# DASHBOARD

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user_name"]
    )

# AI CHAT API

@app.route("/chat", methods=["POST"])
def chat():

    if "user_id" not in session:

        return jsonify({
            "response":"Please login first"
        })

    user_message = request.json["message"]

    ai_response = generate_ai_response(user_message)

    # SAVE CHAT

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO chats(user_id,message,response)

    VALUES(?,?,?)

    """, (
        session["user_id"],
        user_message,
        ai_response
    ))

    conn.commit()

    conn.close()

    return jsonify({
        "response": ai_response
    })

if __name__ == "__main__":

    app.run(debug=True)
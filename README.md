# Intelligent_enterprise_assistant
# Intelligent Enterprise AI Support Assistant

# NAME: SARANYA S
# REGISTER NO:212223220101

# Project Overview

The Intelligent Enterprise AI Support Assistant is a modern AI-powered web application designed to provide enterprise-level IT support and intelligent troubleshooting assistance.

This system integrates with **Ollama + Mistral AI** to deliver real-time AI responses for technical issues such as:

- WiFi Troubleshooting
- Printer Problems
- Password Reset Guidance
- Software Installation Support
- System Performance Issues
- General IT Assistance

The platform includes:

- Secure User Authentication
- Professional Dashboard
- AI Chatbot Interface
- SQLite Database Integration
- Modern Responsive UI


# 🚀 Features

✅ User Registration & Login  
✅ Secure Password Hashing  
✅ Enterprise Dashboard  
✅ AI Chatbot Integration  
✅ Ollama + Mistral AI Support  
✅ Chat History Storage  
✅ Responsive UI Design  
✅ Professional Dark Theme  
✅ Real-Time AI Responses  

# 🛠️ Technologies Used

| Frontend | Backend | AI | Database |
|----------|----------|----|-----------|
| HTML5 | Flask | Ollama | SQLite |
| CSS3 | Python | Mistral AI | |
| JavaScript | | | |



# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/ssaranya27/Intelligent_enterprise_assistant.git
```

---

## 2️⃣ Open Project Folder

```bash
cd Intelligent_enterprise_assistant
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama & Mistral AI

## Download Ollama

https://ollama.com/download

Install normally.

---

## Run Mistral AI

```bash
ollama run mistral
```

Keep Ollama running.

---

# ▶️ Run Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# app.py

```python
from flask import Flask, render_template, request, jsonify, session, redirect

from auth import auth

from models import create_tables, create_connection

from chatbot import generate_ai_response

app = Flask(__name__)

app.secret_key = "enterprise_secret_key"

create_tables()

app.register_blueprint(auth)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user_name"]
    )

@app.route("/chat", methods=["POST"])
def chat():

    if "user_id" not in session:

        return jsonify({
            "response":"Please login first"
        })

    user_message = request.json["message"]

    ai_response = generate_ai_response(user_message)

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
```

---

# index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1.0">

    <title>Enterprise AI Support</title>

    <link rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}">

</head>

<body>

    <nav class="navbar">

        <div class="logo">
            EnterpriseAI
        </div>

        <div class="nav-links">

            <a href="/login">Login</a>

            <a href="/register" class="register-btn">
                Register
            </a>

        </div>

    </nav>

    <section class="hero">

        <div class="hero-left">

            <h1>
                Intelligent Enterprise AI Assistant
            </h1>

            <p>
                Solve technical issues instantly using AI-powered
                enterprise support system integrated with Mistral AI.
            </p>

        </div>

    </section>

</body>

</html>
```

---

# style.css

```css
body{
    background:#0f172a;
    color:white;
    font-family:Arial;
}

.navbar{
    display:flex;
    justify-content:space-between;
    padding:20px 60px;
    background:#111827;
}

.logo{
    font-size:28px;
    font-weight:bold;
}

.nav-links{
    display:flex;
    gap:20px;
}

.register-btn{
    background:#2563eb;
    padding:10px 18px;
    border-radius:10px;
}

.hero{
    padding:100px;
}

.hero h1{
    font-size:60px;
    margin-bottom:20px;
}
```

---

# ⚡ script.js

```javascript
async function sendMessage() {

    const input = document.getElementById("user-input");

    const message = input.value;

    if(message.trim() === "") return;

    const chatBox = document.querySelector(".chat-box");

    chatBox.innerHTML += `

        <div class="user-message">

            ${message}

        </div>

    `;

    input.value = "";

    const response = await fetch("/chat", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    chatBox.innerHTML += `

        <div class="bot-message">

            ${data.response}

        </div>

    `;
}
```
# OUTPUT:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/60828503-2783-4df5-a956-69448fae613e" />

<img width="1920" height="1080" alt="Screenshot (546)" src="https://github.com/user-attachments/assets/080e1fbf-3f6b-4452-adbe-c0252779c170" />

<img width="1920" height="1080" alt="Screenshot (548)" src="https://github.com/user-attachments/assets/ad9faf95-d276-4e0a-b52b-10613be21282" />

<img width="1920" height="1080" alt="Screenshot (550)" src="https://github.com/user-attachments/assets/11b18cfc-b35f-42cf-a5d7-eb1d43ff4797" />



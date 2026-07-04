from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/vehicles")
def vehicles():
    return render_template("vehicles.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)

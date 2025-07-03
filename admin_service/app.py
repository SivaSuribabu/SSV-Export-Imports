from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql_db",
    user="root",
    password="root",
    database="vegetable_store"
)

@app.route("/admin/dashboard")
def dashboard():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) as user_count FROM users")
    user_count = cursor.fetchone()["user_count"]
    cursor.execute("SELECT * FROM orders ORDER BY order_date DESC")
    orders = cursor.fetchall()
    return render_template("dashboard.html", user_count=user_count, orders=orders)

@app.route("/admin/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        email = request.form["email"]
        new_password = request.form["new_password"]
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET password=%s WHERE email=%s",
            (new_password, email)
        )
        db.commit()
        return "Password reset successfully"
    return render_template("reset_password.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)


from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

db = mysql.connector.connect(
    host="mysql_db",
    user="root",
    password="root",
    database="vegetable_store"
)

@app.route("/cart")
def view_cart():
    if "user_id" not in session:
        return redirect("/login")
    cart = session.get("cart", [])
    return render_template("cart.html", cart=cart)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "user_id" not in session:
        return redirect("/login")
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id=%s", (product_id,))
    product = cursor.fetchone()
    if not product or product["quantity"] <= 0:
        return "Product not available"
    cart = session.get("cart", [])
    cart.append(product)
    session["cart"] = cart
    return redirect("/cart")

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "user_id" not in session:
        return redirect("/login")
    cart = session.get("cart", [])
    if request.method == "POST":
        total_amount = sum(item["price"] for item in cart)
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO orders (user_id, order_date, total_amount) VALUES (%s, %s, %s)",
            (session["user_id"], datetime.now(), total_amount)
        )
        order_id = cursor.lastrowid
        for item in cart:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                (order_id, item["id"], 1)
            )
            cursor.execute(
                "UPDATE products SET quantity=quantity-1 WHERE id=%s",
                (item["id"],)
            )
        db.commit()
        session["cart"] = []
        return redirect(url_for("my_orders"))
    return render_template("checkout.html", cart=cart)

@app.route("/my_orders")
def my_orders():
    if "user_id" not in session:
        return redirect("/login")
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM orders WHERE user_id=%s ORDER BY order_date DESC",
        (session["user_id"],)
    )
    orders = cursor.fetchall()
    return render_template("orders.html", orders=orders)

@app.route("/track_order/<int:order_id>")
def track_order(order_id):
    if "user_id" not in session:
        return redirect("/login")
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM orders WHERE id=%s AND user_id=%s",
        (order_id, session["user_id"])
    )
    order = cursor.fetchone()
    return render_template("track_order.html", order=order)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)


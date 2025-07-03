# product_service/app.py

from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql_db",
    user="root",
    password="root",
    database="vegetable_store"
)

@app.route("/products")
def product_list():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT p.id, p.name, p.price, p.quantity, i.image_path FROM products p LEFT JOIN images i ON p.id = i.product_id")
    products = cursor.fetchall()
    return render_template("product_list.html", products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT p.id, p.name, p.price, p.quantity, i.image_path FROM products p LEFT JOIN images i ON p.id = i.product_id WHERE p.id=%s", (product_id,))
    product = cursor.fetchone()
    return render_template("product_detail.html", product=product)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)


🌿 🚀 Vegetable Export & Import Platform – Microservices Documentation
🟢 1️⃣ Auth Service
✅ Purpose
Handles:

Customer registration

Login/logout

Session management

✅ Dependencies
Python 3.9
Flask
MySQL Connector

✅ Install Commands (if running locally):

bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask mysql-connector-python
✅ Ports
5001

✅ How to Build & Run
Local (without Docker):

bash
Copy
Edit
cd auth_service
python3 app.py
Docker:

bash
Copy
Edit
docker build -t auth_service .
docker run -d -p 5001:5001 --network="host" auth_service
Docker Compose:

bash
Copy
Edit
docker-compose up --build
✅ Endpoints
/register – Sign up

/login – Log in

/logout – Log out

🟢 2️⃣ Product Service
✅ Purpose
Show products to customers

Show product detail page

✅ Dependencies
Python 3.9
Flask
MySQL Connector

✅ Install Commands (if running locally):

bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask mysql-connector-python
✅ Ports
5002

✅ Where to Save Images
Directory:

arduino
Copy
Edit
product_service/static/images/
File Naming:
Use descriptive names, e.g.:

Copy
Edit
tomato.png
potato.png
carrot.png
MySQL image_path column:

swift
Copy
Edit
static/images/tomato.png
✅ How to Build & Run
Local:

bash
Copy
Edit
cd product_service
python3 app.py
Docker:

bash
Copy
Edit
docker build -t product_service .
docker run -d -p 5002:5002 --network="host" product_service
Docker Compose:

bash
Copy
Edit
docker-compose up --build
✅ Endpoints
/products – All products

/product/<id> – Details for a single product

🟢 3️⃣ Order Service
✅ Purpose
Manage cart

Checkout

View orders

Track orders

✅ Dependencies
Python 3.9
Flask
MySQL Connector

✅ Install Commands (if running locally):

bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask mysql-connector-python
✅ Ports
5003

✅ How to Build & Run
Local:

bash
Copy
Edit
cd order_service
python3 app.py
Docker:

bash
Copy
Edit
docker build -t order_service .
docker run -d -p 5003:5003 --network="host" order_service
Docker Compose:

bash
Copy
Edit
docker-compose up --build
✅ Endpoints
/cart – View cart

/add_to_cart/<id> – Add to cart

/checkout – Checkout

/my_orders – List all orders

/track_order/<id> – Track order status

🟢 4️⃣ Admin Service
✅ Purpose
Admin dashboard

View users and orders

Reset customer passwords

✅ Dependencies
Python 3.9
Flask
MySQL Connector

✅ Install Commands (if running locally):

bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask mysql-connector-python
✅ Ports
5004

✅ How to Build & Run
Local:

bash
Copy
Edit
cd admin_service
python3 app.py
Docker:

bash
Copy
Edit
docker build -t admin_service .
docker run -d -p 5004:5004 --network="host" admin_service
Docker Compose:

bash
Copy
Edit
docker-compose up --build
✅ Endpoints
/admin/dashboard – Overview of users/orders

/admin/reset_password – Reset user password

🟢 Docker Compose
Start everything together:

bash
Copy
Edit
docker-compose up --build
Ports Recap
Microservice	Port
Auth	5001
Product	5002
Order	5003
Admin	5004
MySQL	3306

🟢 How to Seed Product Data
1️⃣ Save images here:

arduino
Copy
Edit
product_service/static/images/
Example files:

Copy
Edit
tomato.png
potato.png
carrot.png
2️⃣ Insert product and image records:

sql
Copy
Edit
INSERT INTO products (name, price, quantity) VALUES ('Tomato', 25.00, 100);
INSERT INTO images (product_id, image_path) VALUES (1, 'static/images/tomato.png');
🟢 Example Commands to Install Docker
✅ Install Docker & Docker Compose (Ubuntu):

bash
Copy
Edit
sudo apt update
sudo apt install docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker
✅ Verify Docker installation:

bash
Copy
Edit
docker --version
docker-compose --version
🟢 Example Commands to Build All Containers
bash
Copy
Edit
docker-compose up --build
Rebuild specific service:

bash
Copy
Edit
docker-compose build auth_service
docker-compose up auth_service
Stop containers:

bash
Copy
Edit
docker-compose down
🟢 Quick Verification URLs
Service	URL
Auth	http://localhost:5001
Product	http://localhost:5002/products
Order	http://localhost:5003/cart
Admin	http://localhost:5004/admin/dashboard

✅ This is now complete and production-ready documentation you can paste into your project README.md.

If you’d like, I can also:

Provide Docker Compose YAML in detail

Help you build AWS deployment steps

Write CI/CD pipeline scripts

# Task: Build a "Cafe and WiFi" API with Postman Documentation

## Objective
Create a RESTful API for managing cafes and their WiFi information. Document the API endpoints using Postman, including descriptions, request/response examples, and parameters.

---

## Steps

### 1. Set Up the Flask Application
#### Tasks:
- Create a Flask app with routes to handle CRUD operations for cafes.
- Use SQLAlchemy to manage the database of cafes, with the following fields:
  - `id` (Integer, primary key)
  - `name` (String, required)
  - `location` (String, required)
  - `wifi_quality` (Integer, optional)
  - `coffee_price` (Float, optional)

#### Example Code:
```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    wifi_quality = db.Column(db.Integer, nullable=True)
    coffee_price = db.Column(db.Float, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to the Cafe and WiFi API"
```

---

### 2. Implement API Endpoints
#### Tasks:
- Implement the following endpoints:
  - `GET /cafes` - Retrieve a list of all cafes.
  - `GET /cafe/<id>` - Retrieve a specific cafe by ID.
  - `POST /cafe` - Add a new cafe.
  - `PUT /cafe/<id>` - Update a specific cafe's information.
  - `DELETE /cafe/<id>` - Delete a specific cafe.

#### Example Code:
```python
@app.route('/cafes', methods=['GET'])
def get_cafes():
    cafes = Cafe.query.all()
    return jsonify([{
        "id": cafe.id,
        "name": cafe.name,
        "location": cafe.location,
        "wifi_quality": cafe.wifi_quality,
        "coffee_price": cafe.coffee_price
    } for cafe in cafes])

@app.route('/cafe/<int:id>', methods=['GET'])
def get_cafe(id):
    cafe = Cafe.query.get_or_404(id)
    return jsonify({
        "id": cafe.id,
        "name": cafe.name,
        "location": cafe.location,
        "wifi_quality": cafe.wifi_quality,
        "coffee_price": cafe.coffee_price
    })

@app.route('/cafe', methods=['POST'])
def add_cafe():
    data = request.get_json()
    new_cafe = Cafe(
        name=data["name"],
        location=data["location"],
        wifi_quality=data.get("wifi_quality"),
        coffee_price=data.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"message": "Cafe added successfully"}), 201

@app.route('/cafe/<int:id>', methods=['PUT'])
def update_cafe(id):
    cafe = Cafe.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        cafe.name = data["name"]
    if "location" in data:
        cafe.location = data["location"]
    if "wifi_quality" in data:
        cafe.wifi_quality = data["wifi_quality"]
    if "coffee_price" in data:
        cafe.coffee_price = data["coffee_price"]
    db.session.commit()
    return jsonify({"message": "Cafe updated successfully"})

@app.route('/cafe/<int:id>', methods=['DELETE'])
def delete_cafe(id):
    cafe = Cafe.query.get_or_404(id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"message": "Cafe deleted successfully"})
```

---

### 3. Document API Using Postman
#### Tasks:
- Create a Postman collection with the following details:
  - `GET /cafes`
    - Description: Fetch all cafes in the database.
    - Example Response:
      ```json
      [
          {
              "id": 1,
              "name": "Cafe One",
              "location": "Downtown",
              "wifi_quality": 5,
              "coffee_price": 3.50
          }
      ]
      ```
  - `GET /cafe/<id>`
    - Description: Fetch details of a specific cafe by ID.
  - `POST /cafe`
    - Description: Add a new cafe to the database.
    - Example Request Body:
      ```json
      {
          "name": "New Cafe",
          "location": "Uptown",
          "wifi_quality": 4,
          "coffee_price": 4.00
      }
      ```
  - `PUT /cafe/<id>`
    - Description: Update details of an existing cafe.
    - Example Request Body:
      ```json
      {
          "wifi_quality": 3
      }
      ```
  - `DELETE /cafe/<id>`
    - Description: Delete a cafe by ID.

- Include headers, parameters, and example responses for each endpoint.
- Export the Postman collection and attach it to the project.

---

## Deliverables
1. Flask API with the following endpoints:
   - `GET /cafes`
   - `GET /cafe/<id>`
   - `POST /cafe`
   - `PUT /cafe/<id>`
   - `DELETE /cafe/<id>`
2. SQLite database with the `Cafe` model.
3. Postman collection documenting all API endpoints.

---

## Notes
- Ensure that all endpoints return proper HTTP status codes (e.g., 200, 201, 404).
- Validate input data where necessary.
- Test all endpoints before creating the Postman documentation.
- Ensure the Postman documentation includes a clear description for each endpoint.


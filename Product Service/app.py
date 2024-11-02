# app.py for Product Service
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def products():
    products = [
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Phone", "price": 499},
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

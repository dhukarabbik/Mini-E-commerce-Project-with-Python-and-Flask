# app.py for Frontend Service
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the e-commerce frontend!"

@app.route('/products')
def get_products():
    try:
        response = requests.get('http://product-service:5001/products')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": "Unable to fetch products", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
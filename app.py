from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Set up audit logging
logging.basicConfig(filename='audit.log', level=logging.INFO,
                     format='%(asctime)s %(message)s')

def calculate_quote(age, coverage_type):
    base_rate = 50
    if age < 25:
        risk_multiplier = 1.5
    elif age < 50:
        risk_multiplier = 1.0
    else:
        risk_multiplier = 1.3

    coverage_multiplier = {"basic": 1.0, "standard": 1.5, "premium": 2.0}
    multiplier = coverage_multiplier.get(coverage_type, 1.0)

    return round(base_rate * risk_multiplier * multiplier, 2)

@app.route('/quote', methods=['GET'])
def get_quote():
    age = int(request.args.get('age', 30))
    coverage_type = request.args.get('coverage', 'basic')

    quote = calculate_quote(age, coverage_type)

    logging.info(f"Quote requested - age: {age}, coverage: {coverage_type}, quote: ${quote}")

    return jsonify({
        "age": age,
        "coverage_type": coverage_type,
        "monthly_quote": quote
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

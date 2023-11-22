from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/multiply', methods=['GET'])
def multiply():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = num1 * num2
    return jsonify({'result': result})

@app.route('/subtract', methods=['GET'])
def subtract():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = num1 - num2
    return jsonify({'result': result})

@app.route('/divide', methods=['GET'])
def divide():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    if num2 == 0:
        return jsonify({'error': 'Division by zero is not allowed.'}), 400
    result = num1 / num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

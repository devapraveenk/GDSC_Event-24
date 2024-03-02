from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dev', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both numbers'}), 400

    try:
        result = float(num1) * float(num2)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input, please provide valid numbers'}), 400

if __name__ == '__main__':
    app.run(debug=True)

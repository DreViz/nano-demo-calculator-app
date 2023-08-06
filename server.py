from flask import Flask,jasonify,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']

        try:
            result = num1 + num2
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({"error": "Invalid input"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

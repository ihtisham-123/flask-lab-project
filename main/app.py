from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    return jsonify({"received": data}), 201

@app.route('/cicd-check')
def cicd_check():
    return "CI/CD is working!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    result = {"result": f"Generated content for: {prompt}"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

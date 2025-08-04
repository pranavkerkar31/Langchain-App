from flask import Flask, render_template, jsonify, request
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        return jsonify({"result": "OpenAI API key not found."}), 500

    try:
        chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.7)
        response = chat([HumanMessage(content=prompt)])
        result = response.content
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)

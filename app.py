from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
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

    google_api_key = os.getenv("GEMINI_API_KEY")

    chat = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  
        google_api_key=google_api_key,
        temperature=0.7,
    )

    response = chat.invoke([HumanMessage(content=prompt)])
    return jsonify({"result": response.content})

if __name__ == '__main__':
    app.run(debug=True)

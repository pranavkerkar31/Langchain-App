<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Google_Gemini_logo.svg/1200px-Google_Gemini_logo.svg.png" alt="Gemini" height="60"/>
  &nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/langchain-ai/langchain/main/docs/static/img/logo.png" alt="LangChain" height="60"/>
  &nbsp;&nbsp;
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python" height="60"/>
  &nbsp;&nbsp;
  <img src="https://flask.palletsprojects.com/en/3.0.x/_images/flask-logo.png" alt="Flask" height="60"/>
</p>

# 🚀 AI Content Generator

A simple web app that uses **Gemini API**, **LangChain**, **Python**, and **Flask** to generate content based on user prompts in real time.

---

## 📦 Installation

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
2️⃣ Create & activate virtual environment

python -m venv env
Windows:
.\env\Scripts\activate

macOS/Linux:
source env/bin/activate

3️⃣ Install the dependencies
pip install -r requirements.txt

4️⃣ Install additional packages
pip install langchain-google-genai flask python-dotenv

5️⃣ Set up your .env file
Create a .env file in the root directory and add your Google API key:


GEMINI_API_KEY=your_geminin_api_key_here

▶️ Running the Application
Launch the Flask app:
python app.py
Then open your browser at http://127.0.0.1:5000 to start generating content!

⚙️ Tech Stack
Google Gemini API: For advanced AI content generation.

LangChain: To orchestrate the prompt-to-response pipeline.

Python + Flask: Backend server handling requests and responses.

📜 License
This project is licensed under the MIT License.


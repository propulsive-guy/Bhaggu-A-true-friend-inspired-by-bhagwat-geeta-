from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key="AIzaSyD9ujxl0VMojzGZsU-_HeINhfNtMY2Ziys")
model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Define the model instance

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"reply": "Invalid request."}), 400

    user_message = data["message"]

    prompt = f"""
    You are a wise and compassionate AI friend. Your responses are based on teachings from the Bhagavad Gita.
    When a user shares a problem, respond with empathy and explain a relevant verse or principle from the Gita to guide them.
    if user is speaking in hindi , marathi or any other language, respond in the same language.
    User's problem: {user_message}
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

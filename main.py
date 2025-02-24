from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

difficulty_levels = ["beginner", "intermediate", "advance"]
styles = ["formal", "semi-formal", "non-formal", "slang"]

def generate_response(user_input, difficulty, style):
    if difficulty not in difficulty_levels:
        difficulty = "beginner"
    if style not in styles:
        style = "formal"
    
    prompt = f"You are a chatbot that speaks English at a {difficulty} level with a {style} style. Respond to: {user_input}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def evaluate_conversation(user_input, ai_response):
    eval_prompt = f"Evaluate this conversation in Indonesian: User: {user_input} AI: {ai_response}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an English tutor who provides constructive feedback in Indonesian."},
                  {"role": "user", "content": eval_prompt}]
    )
    return response.choices[0].message.content

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    difficulty = data.get("difficulty", "beginner")
    style = data.get("style", "formal")
    evaluate = data.get("evaluate", False)
    
    ai_response = generate_response(user_input, difficulty, style)
    evaluation = evaluate_conversation(user_input, ai_response) if evaluate else None
    
    return jsonify({"response": str(ai_response), "evaluation": str(evaluation), "available_difficulty": difficulty_levels, "available_styles": styles})

if __name__ == "__main__":
    app.run(debug=True)

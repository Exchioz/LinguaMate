import logging
from openai import OpenAI
from .config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)
model = Config.OPENAI_MODEL

difficulty_levels = ["beginner", "intermediate", "advance"]
styles = ["formal", "semi-formal", "non-formal"]

def generate_response(user_input: str, difficulty: str, style: str) -> str:
    prompt = (
        f"You are a chatbot that helps users learn English. "
        f"Speak at a {difficulty} level with a {style} style. "
        f"User: {user_input}"
    )
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.exception("Error in generate_response")
        return f"Error: {str(e)}"

def evaluate_conversation(user_input: str, ai_response: str) -> str:
    eval_prompt = (
        f"As an English tutor, analyze the conversation between the user and the AI."
        f"Provide constructive feedback in Indonesian, focusing on grammar, vocabulary, and fluency."
        f"Conversation:\nUser: {user_input}\nAI: {ai_response}"
    )
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an English tutor providing feedback in Indonesian."},
                {"role": "user", "content": eval_prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.exception("Error in evaluate_conversation")
        return f"Error: {str(e)}"

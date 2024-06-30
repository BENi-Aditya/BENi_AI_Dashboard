import openai
from dotenv import load_dotenv
import os

load_dotenv()
class QuestionMakerBot:
    def __init__(self):
        self.api_key = os.getenv("self.api_key")
        self.model = "gpt-3.5-turbo"
        openai.api_key = self.api_key
        self.conversation_history = []

    def get_response(self, user_input):
        try:
            self.conversation_history.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an assistant specialized in making practice questions from the topic provided by the user, don't stray away from the topics provided by the user and only provide questions from reliable sources. Make sure that whenever the user asks any new questions try to relate it to that user's previous questions and the answers you gave, make sure you answer according to your previous interactions."},
                ] + self.conversation_history,
                temperature=0.7,
                max_tokens=250,
                stop=None
            )
            response_message = response.choices[0].message['content'].strip()
            self.conversation_history.append({"role": "assistant", "content": response_message})
            return response_message
        except Exception as e:
            return f"Error: {e}"

# Create an instance of the QuestionMakerBot class
question_maker_bot = QuestionMakerBot()

def handle_question_maker(user_input):
    return question_maker_bot.get_response(user_input)
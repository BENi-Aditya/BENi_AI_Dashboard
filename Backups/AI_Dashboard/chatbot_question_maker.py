import openai
import os

class QuestionMakerBot:
    def __init__(self):
        self.api_key = "sk-proj-hrm9UjAvm6gFl82PMqBaT3BlbkFJVuRv86PKZ7T8kOdsuDsk"
        self.model = "gpt-3.5-turbo"
        openai.api_key = self.api_key

    def get_response(self, user_input):
        try:
            messages = [
                {"role": "system", "content": "You are an assistant specialized in creating questions for educational purposes. Generate relevant and thought-provoking questions based on the given topic or document."},
                {"role": "user", "content": user_input}
            ]
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=150,
                stop=None
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return f"Error: {e}"

# Create an instance of the QuestionMakerBot class
question_maker_bot = QuestionMakerBot()

def handle_question_maker(user_input):
    return question_maker_bot.get_response(user_input)
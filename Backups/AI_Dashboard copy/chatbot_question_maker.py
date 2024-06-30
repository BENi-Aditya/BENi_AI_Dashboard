# chatbot_question_maker.py
import openai

# Initialize the OpenAI API client
openai.api_key = 'sk-proj-hrm9UjAvm6gFl82PMqBaT3BlbkFJVuRv86PKZ7T8kOdsuDsk'

def handle_question_maker(user_input):
    # This function generates questions based on the user input
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate questions based on the following input: {user_input}",
        max_tokens=100
    )
    return response.choices[0].text.strip()
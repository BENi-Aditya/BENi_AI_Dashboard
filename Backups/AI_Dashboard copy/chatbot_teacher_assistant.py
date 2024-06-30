import openai

openai.api_key = 'sk-proj-hrm9UjAvm6gFl82PMqBaT3BlbkFJVuRv86PKZ7T8kOdsuDsk'

def handle_teacher_assistant(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Teacher Assistant Bot: {message}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
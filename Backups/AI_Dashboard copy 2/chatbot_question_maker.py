import openai

def handle_question_maker(user_input):
    openai.api_key = "sk-proj-hrm9UjAvm6gFl82PMqBaT3BlbkFJVuRv86PKZ7T8kOdsuDsks"  # Replace with your actual OpenAI API key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a question maker bot."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']
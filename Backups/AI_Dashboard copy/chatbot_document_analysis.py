# chatbot_document_analysis.py
import openai
import PyPDF2

# Initialize the OpenAI API client
openai.api_key = 'sk-proj-hrm9UjAvm6gFl82PMqBaT3BlbkFJVuRv86PKZ7T8kOdsuDsks'

def extract_text_from_pdf(pdf_path):
    # This function extracts text from a PDF file
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
    text = ""
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extract_text()
    return text

def handle_document_analysis(user_input, pdf_path=None):
    # This function analyzes documents based on the user input
    if pdf_path:
        document_text = extract_text_from_pdf(pdf_path)
        prompt = f"Analyze the following document based on the input: {user_input}\nDocument text: {document_text}"
    else:
        prompt = f"Analyze the following document based on the input: {user_input}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
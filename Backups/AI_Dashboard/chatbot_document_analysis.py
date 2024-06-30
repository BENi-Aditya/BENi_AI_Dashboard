import openai
import os
from PyPDF2 import PdfReader

class DocumentAnalysisBot:
    def __init__(self):
        self.api_key = "sk-proj-hrm9UjAvm6gFl82PMqBaT3BlbkFJVuRv86PKZ7T8kOdsuDsk"
        self.model = "gpt-3.5-turbo"
        openai.api_key = self.api_key

    def extract_text_from_pdf(self, pdf_path):
        text = ""
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text += page.extract_text()
        except Exception as e:
            return f"Error extracting text from PDF: {e}"
        return text

    def get_response(self, extracted_text, user_input):
        try:
            messages = [
                {"role": "system", "content": "You are an assistant specialized in analyzing documents and generating answers based on the document content and user queries."},
                {"role": "system", "content": f"Document Content: {extracted_text}"},
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
            return f"Error getting response from OpenAI: {e}"

# Create an instance of the DocumentAnalysisBot class
document_analysis_bot = DocumentAnalysisBot()

def handle_document_analysis(file_path, user_input):
    extracted_text = ""
    if file_path:
        extracted_text = document_analysis_bot.extract_text_from_pdf(file_path)
        if extracted_text.startswith("Error"):
            return extracted_text
    return document_analysis_bot.get_response(extracted_text, user_input)
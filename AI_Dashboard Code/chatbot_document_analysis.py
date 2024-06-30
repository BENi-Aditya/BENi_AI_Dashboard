import openai
import fitz  # PyMuPDF
from dotenv import load_dotenv
import os

load_dotenv()

class DocumentAnalysisBot:
    def __init__(self):
        self.api_key = os.getenv("self.api_key")        
        self.model = "gpt-3.5-turbo"
        openai.api_key = self.api_key
        self.conversation_history = []

    def get_response(self, user_input, file_content=None):
        try:
            bot_description = (
                "You are an assistant specialized in analyzing and interpreting documents. "
                "Your primary responsibilities include:\n\n"
                "1. Analyzing Documents: Provide detailed analysis and interpretation of various documents such as research papers, textbooks, lesson plans, and more. Highlight key points, summarize important information, and offer insights to help users understand the content better.\n"
                "2. Answering Questions: Provide clear and concise answers to questions related to the content of the provided documents.\n"
                "3. Providing Study Tips and Strategies: Offer effective study techniques, time management strategies, and tips for academic success based on the analyzed documents.\n\n"
                "Tone and Style:\n\n"
                "• Professional and Knowledgeable: Maintain a tone that is professional, authoritative, and demonstrates a strong understanding of educational content.\n"
                "• Clear and Concise: Provide information in a clear, concise, and easy-to-understand manner, avoiding unnecessary jargon or complexity.\n"
            )

            if file_content:
                self.conversation_history.append({"role": "system", "content": f"Document content: {file_content}"})

            self.conversation_history.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": bot_description},
                ] + self.conversation_history,
                temperature=0.7,
                max_tokens=300,
                stop=None
            )
            response_message = response.choices[0].message['content'].strip()
            self.conversation_history.append({"role": "assistant", "content": response_message})
            return response_message
        except Exception as e:
            return f"Error: {e}"

# Create an instance of the DocumentAnalysisBot class
document_analysis_bot = DocumentAnalysisBot()

def handle_document_analysis(file_path, user_input):
    file_content = None
    if file_path:
        try:
            with fitz.open(file_path) as doc:
                file_content = ""
                for page in doc:
                    file_content += page.get_text()
        except Exception as e:
            return f"Error reading file: {e}"
    return document_analysis_bot.get_response(user_input, file_content)